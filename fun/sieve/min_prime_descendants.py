import sys

from concurrent.futures import ProcessPoolExecutor
from itertools import islice, repeat
from multiprocessing import Manager
from reduced_residue_system import (all_reduced_residue_system_primorial,
                                    min_prime_descendant, primoradic,
                                    reduced_residue_system_primorial_new)


def report_intersting_descendants(chunk, result_queue, completion_queue):
    for residue, i in chunk:
        descendant, j = min_prime_descendant(residue, i)
        if j - i > 1 and primoradic(descendant)[-2] != 0:
            result_queue.put((residue, i, descendant, j))
    completion_queue.put(None)


def main():
    chunksize = 10000
    max_outstanding = 100
    if len(sys.argv) > 1:
        i = int(sys.argv[1])
        generator = zip(reduced_residue_system_primorial_new(i), repeat(i))
    else:
        generator = all_reduced_residue_system_primorial()

    with Manager() as manager, ProcessPoolExecutor() as executor:
        result_queue = manager.Queue()
        completion_queue = manager.Queue()
        num_outstanding = 0

        while True:
            # Drain the completion queue to get the number of outstanding processes.
            while not completion_queue.empty():
                completion_queue.get()
                num_outstanding -= 1

            # Wait until a process completes if the number of outstanding
            # processes is at the maximum.
            if num_outstanding == max_outstanding:
                completion_queue.get()
                num_outstanding -= 1

            chunk = tuple(islice(generator, chunksize))
            if len(chunk) > 0:
                executor.submit(report_intersting_descendants, chunk,
                                result_queue, completion_queue)
                num_outstanding += 1
            while not result_queue.empty():
                residue, i, descendant, j = result_queue.get()
                print(residue, i, descendant, j, primoradic(residue),
                      primoradic(descendant))
                if j - i > 2:
                    return
            if num_outstanding == 0:
                break


if __name__ == '__main__':
    main()

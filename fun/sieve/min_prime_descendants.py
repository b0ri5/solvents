import sys

from concurrent.futures import ProcessPoolExecutor
from itertools import count, islice, repeat
from multiprocessing import Manager
from reduced_residue_system import (all_reduced_residue_system_primorial,
                                    ancestors, interesting_composites,
                                    min_prime_descendant, primoradic,
                                    random_rrsp,
                                    reduced_residue_system_primorial_new)


def report_intersting_descendants(chunk, result_queue, completion_queue):
    for residue, i in chunk:
        descendant, j = min_prime_descendant(residue, i)
        if j - i > 1:
            result_queue.put((residue, i, descendant, j))
    completion_queue.put(None)


def exhaustive():
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
                return


def interesting():
    for i in count(start=4):
        print('Checking interesting composites at', i)
        for residue in interesting_composites(i):
            print(residue)
            descendant, j = min_prime_descendant(residue, i)
            if j - i > 1:
                print(residue, i, descendant, j, primoradic(residue),
                      primoradic(descendant))
            if j - i > 2:
                return


def random():
    while True:
        residue = random_rrsp(80)
        print('Trying out', residue)
        for i, ancestor in enumerate(ancestors(residue), start=1):
            descendant, j = min_prime_descendant(ancestor, i)
            if j - i > 1:
                print(ancestor, i, descendant, j, primoradic(ancestor),
                      primoradic(descendant))
            if j - i > 2:
                return


def main():
    if sys.argv[1] == 'interesting':
        interesting()
    elif sys.argv[1] == 'random':
        random()
    else:
        exhaustive()


if __name__ == '__main__':
    main()

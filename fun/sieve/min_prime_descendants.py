from concurrent.futures import ProcessPoolExecutor
from itertools import islice
from multiprocessing import Manager
from reduced_residue_system import min_prime_descendant, all_reduced_residue_system_primorial


def report_intersting_descendants(chunk, result_queue, completion_queue):
    for residue, i in chunk:
        descendant, j = min_prime_descendant(residue, i)
        if j - i > 1:
            result_queue.put((residue, i, descendant, j))
    completion_queue.put(None)


def main():
    chunksize = 10000
    max_outstanding = 100
    manager = Manager()
    result_queue = manager.Queue()
    completion_queue = manager.Queue()
    with ProcessPoolExecutor() as executor:
        generator = all_reduced_residue_system_primorial()
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
            executor.submit(report_intersting_descendants, chunk, result_queue,
                            completion_queue)
            num_outstanding += 1
            while not result_queue.empty():
                residue, i, descendant, j = result_queue.get()
                print(residue, i, descendant, j)
                if j - i > 2:
                    return


if __name__ == '__main__':
    main()

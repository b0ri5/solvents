from concurrent.futures import ProcessPoolExecutor
from itertools import count, islice
from multiprocessing import Queue
from reduced_residue_system import min_prime_descendant, all_reduced_residue_system_primorial


def report_intersting_descendants(chunk, queue):
    for residue, i in chunk:
        descendant, j = min_prime_descendant(residue, i)
        if j - i > 1:
            queue.put((residue, i, descendant, j))


def main():
    chunksize = 1000
    queue = Queue()
    with ProcessPoolExecutor() as executor:
        generator = all_reduced_residue_system_primorial()
        while True:
            chunk = islice(generator, chunksize)
            executor.submit(report_intersting_descendants, chunk, queue)
            while not queue.empty():
                print(*queue.get())


if __name__ == '__main__':
    main()

from concurrent.futures import ProcessPoolExecutor
from itertools import count, starmap
from reduced_residue_system import min_prime_descendant, all_reduced_residue_system_primorial


def star_min_prime_descendant(residue_i):
    return min_prime_descendant(*residue_i)


def main():
    for (residue, i), (descendant, j) in zip(
            all_reduced_residue_system_primorial(),
            map(star_min_prime_descendant,
                all_reduced_residue_system_primorial())):
        if j - i > 1:
            print(residue, i, descendant, j)


if __name__ == '__main__':
    main()

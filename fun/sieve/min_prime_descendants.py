from itertools import count
from reduced_residue_system import min_prime_descendant, reduced_residue_system_primorial_new
from sympy import isprime


def main():
    for i in count(start=2):
        for residue in reduced_residue_system_primorial_new(i):
            if isprime(residue):
                continue
            descendant, j = min_prime_descendant(residue, i)
            if j - i > 1:
                print(residue, i, descendant, j)


if __name__ == '__main__':
    main()

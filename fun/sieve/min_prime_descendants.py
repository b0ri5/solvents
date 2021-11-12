from itertools import count
from reduced_residue_system import min_prime_descendant, reduced_residue_system_primorial
from sympy import isprime


def main():
    # A map from residues to the i at which they were first seen
    seen_residues = {}
    for i in count(start=2):
        for residue in sorted(reduced_residue_system_primorial(i)):
            if residue in seen_residues or isprime(residue):
                continue
            seen_residues[residue] = i
            descendant, j = min_prime_descendant(residue, i)
            if j - i > 1 or len(seen_residues) % 1000 == 0:
                print(residue, i, descendant, j)


if __name__ == '__main__':
    main()

import math

from reduced_residue_system import (ancestors_compositeness, random_rrsp,
                                    reduced_residue_system_primorial)
from sympy import isprime, prime


def there_are_enough_non_two_primes():

    def num_rrsp(i):
        return math.prod((prime(i) - 1 for i in range(1, i + 1)))

    def num_rrsp_2(i):
        return math.prod((prime(i) - 2 for i in range(2, i + 1)))

    def num_prime_rrsp(i):
        return sum(isprime(r) for r in reduced_residue_system_primorial(i))

    for i in range(1, 10):
        num_rrsp_i = num_rrsp(i)
        num_rrsp_2_i = num_rrsp_2(i)
        print(num_rrsp_i, num_rrsp_2_i, num_rrsp_i - num_rrsp_2_i,
              num_prime_rrsp(i))


def ancestors_compositeness_counts():
    depth = 80
    counts = [0 for _ in range(depth)]
    for i in range(1000):
        for j, is_composite in enumerate(
                ancestors_compositeness(random_rrsp(depth))):
            if is_composite:
                counts[j] += 1
        print(i, counts)


def main():
    there_are_enough_non_two_primes()


if __name__ == '__main__':
    there_are_enough_non_two_primes()

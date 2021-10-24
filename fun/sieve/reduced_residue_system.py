# See https://en.wikipedia.org/wiki/Reduced_residue_system

from collections import namedtuple
from functools import cache
from math import gcd
from sympy import isprime, prime, primerange, primorial


def _reduced_residue_system_primorial_brute_force(i):
    system = set()
    primorial_i = primorial(i)
    for k in range(1, primorial_i):
        if gcd(primorial_i, k) == 1:
            system.add(k)
    return frozenset(system)


@cache
def reduced_residue_system_primorial(i):
    if i == 1:
        return frozenset({1})
    previous_rrs = reduced_residue_system_primorial(i - 1)
    prime_i = prime(i)
    previous_primorial = primorial(i - 1)
    rrs = set()
    for residue in previous_rrs:
        for k in range(0, prime_i):
            candidate = previous_primorial * k + residue
            if candidate % prime_i != 0:
                rrs.add(candidate)
    return frozenset(rrs)


def filter_twos(rrs):
    # A "two" is a residue that corresponds to a 2 in the corresponding dRRS.
    # That means that r and r + 2 is in the RRS.
    twos = {r for r in rrs if r + 2 in rrs}
    twos.add(max(rrs))
    return frozenset(twos)


@cache
def reduced_residue_system_primorial_twos(i):
    if i == 1:
        return frozenset({1})
    previous_rrs = reduced_residue_system_primorial_twos(i - 1)
    prime_i = prime(i)
    previous_primorial = primorial(i - 1)
    rrs = set()
    for residue in previous_rrs:
        for k in range(0, prime_i):
            candidate = previous_primorial * k + residue
            if candidate % prime_i != 0 and (candidate + 2) % prime_i != 0:
                rrs.add(candidate)
    return frozenset(rrs)


def filter_twin_primes(rrs):
    twin_primes = {r for r in rrs if isprime(r) and isprime(r + 2)}
    return frozenset(twin_primes)


def twin_primes_between_prime_and_primorial(i):
    if i == 1:
        # The applied gap of rrs(1) = {1} is {3} so it still should count
        return {1}
    return [p for p in primerange(prime(i + 1), primorial(i)) if isprime(p + 2)]


def prime_and_composite_between_prime_and_primorial(i):
    return [
        p for p in primerange(prime(i + 1), primorial(i))
        if not isprime(p + 2) and gcd(p + 2, primorial(i)) == 1
    ]


def composite_and_prime_between_prime_and_primorial(i):
    return [
        r for r in range(prime(i + 1), primorial(i))
        if not isprime(r) and isprime(r + 2) and gcd(r, primorial(i)) == 1
    ]


def composite_and_composite_between_prime_and_primorial(i):
    return [
        r for r in range(prime(i + 1), primorial(i))
        if not isprime(r) and not isprime(r + 2) and
        gcd(r, primorial(i)) == 1 and gcd(r + 2, primorial(i)) == 1
    ]


# The elements that the residue r in rss(i) contributes to rss(i + 1)
def children(residue, i):
    primorial_i = primorial(i)
    next_prime = prime(i + 1)
    for k in range(0, next_prime):
        candidate = primorial_i * k + residue
        if candidate % next_prime != 0:
            yield candidate


def reduced_residue_system_primorial_gaps(i):
    rrs = sorted(reduced_residue_system_primorial(i))
    gaps = []
    for k in range(1, len(rrs)):
        gaps.append(rrs[k] - rrs[k - 1])
    gaps.append(2)
    return gaps


def reduced_residue_system_primorial_applied_gaps(i):
    rrs = sorted(reduced_residue_system_primorial(i))
    gaps = reduced_residue_system_primorial_gaps(i)
    return [rrs[k] + gaps[k] for k in range(len(rrs))]


TwoClassification = namedtuple('TwoClassification', [
    'composite_to_composite', 'composite_to_prime', 'prime_to_composite',
    'prime_to_prime'
])


def reduced_residue_system_primorial_two_classification(i):
    # One needs to be special-cased because this is implemented via RRS
    # and not applied gaps.
    if i == 1:
        return TwoClassification(composite_to_composite=0,
                                 composite_to_prime=0,
                                 prime_to_composite=0,
                                 prime_to_prime=1)
    rrs = reduced_residue_system_primorial_twos(i)
    composite_to_composite = 0
    composite_to_prime = 0
    prime_to_composite = 0
    prime_to_prime = 0
    for residue in rrs:
        if isprime(residue):
            if isprime(residue + 2):
                prime_to_prime += 1
            else:
                prime_to_composite += 1
        else:
            if isprime(residue + 2):
                composite_to_prime += 1
            else:
                composite_to_composite += 1
    return TwoClassification(composite_to_composite=composite_to_composite,
                             composite_to_prime=composite_to_prime,
                             prime_to_composite=prime_to_composite,
                             prime_to_prime=prime_to_prime)

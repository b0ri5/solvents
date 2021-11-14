# See https://en.wikipedia.org/wiki/Reduced_residue_system

from collections import deque, namedtuple
from functools import cache
from math import gcd
from sympy.ntheory.modular import crt
from sympy import isprime, nextprime, primepi, primerange

import sympy


@cache
def prime(i):
    return sympy.prime(i)


@cache
def primorial(i):
    if i == 1:
        return 2
    return prime(i) * sympy.primorial(i - 1)


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
    # The children are all of
    #   primorial(i - 1) * k + r
    # for 0 <= k < prime(i) excepting the single k that results in a value
    # congruent to 0 modulo prime(i).
    # The k to skip is (primorial(i - 1) % prime(i)) * k + r = 0 (mod prime(i))
    inv = primorial_multiplicative_inverse(i - 1)
    for residue in previous_rrs:
        skipped = (inv * (prime_i - (residue % prime_i))) % prime_i
        primorial_multiples = set(range(prime_i))
        primorial_multiples.remove(skipped)
        for k in primorial_multiples:
            rrs.add(previous_primorial * k + residue)
    return frozenset(rrs)


def filter_twos(rrs):
    # A "two" is a residue that corresponds to a 2 in the corresponding dRRS.
    # That means that r and r + 2 is in the RRS.
    twos = {r for r in rrs if r + 2 in rrs}
    twos.add(max(rrs))
    return frozenset(twos)


# This is https://oeis.org/A079276
@cache
def primorial_multiplicative_inverse(i):
    return pow(primorial(i) % prime(i + 1), -1, prime(i + 1))


@cache
def reduced_residue_system_primorial_twos(i):
    if i == 1:
        return frozenset({1})
    previous_rrs = reduced_residue_system_primorial_twos(i - 1)
    prime_i = prime(i)
    previous_primorial = primorial(i - 1)
    rrs = set()
    # The children are all of
    #   primorial(i - 1) * k + r
    # for 0 <= k < prime(i) excepting the single k that results in a value
    # congruent to 0 modulo prime(i).
    # The ks to skip are (primorial(i - 1) % prime(i)) * k + r = 0 or -2 (mod prime(i))
    inv = primorial_multiplicative_inverse(i - 1)
    for residue in previous_rrs:
        skipped_zero = (inv * (prime_i - (residue % prime_i))) % prime_i
        skipped_negative_two = (inv * (prime_i -
                                       ((residue + 2) % prime_i))) % prime_i
        primorial_multiples = set(range(prime_i))
        primorial_multiples.remove(skipped_zero)
        primorial_multiples.remove(skipped_negative_two)
        for k in primorial_multiples:
            rrs.add(previous_primorial * k + residue)
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
# Children are yielded in sorted order.
def children(residue, i):
    next_prime = prime(i + 1)
    # The children are all of
    #   primorial(i) * k + r
    # for 0 <= k < prime(i + 1) excepting the single k that results in a value
    # congruent to 0 modulo prime(i + 1).
    # The k to skip is (primorial(i) % prime(i + 1)) * k + r = 0 (mod prime(i + 1))
    inv = primorial_multiplicative_inverse(i)
    skipped = (inv * (next_prime - (residue % next_prime))) % next_prime
    primorial_multiples = set(range(next_prime))
    primorial_multiples.remove(skipped)
    primorial_i = primorial(i)
    for k in primorial_multiples:
        yield primorial_i * k + residue


# The minimum element that the residue r in rss(i) contributes to rss(i + 1)
def min_child(residue, i):
    next_prime = prime(i + 1)
    # The minimum child is r or primorial(i) + r.
    # The one to skip is (primorial(i) % prime(i + 1)) * k + r = 0 (mod prime(i + 1))
    inv = primorial_multiplicative_inverse(i)
    skipped = (inv * (next_prime - (residue % next_prime))) % next_prime
    primorial_i = primorial(i)
    if skipped == 0:
        return primorial_i + residue
    return residue


# Keep taking the min child until a prime is found.
def min_extension(residue, i):
    if residue == 1 or isprime(residue):
        return (residue, i)
    return min_extension(min_child(residue, i), i + 1)


# Look at each descendant in a breadth first manner until a prime is found.
def min_prime_descendant(residue, i):
    if isprime(residue):
        return (residue, i)
    queue = deque()
    queue.appendleft((residue, i))
    while True:
        residue, i = queue.pop()
        for child in children(residue, i):
            if isprime(child):
                return (child, i + 1)
            queue.appendleft((child, i + 1))


def primoradic(num):
    if num == 0:
        return (0,)
    # Couldn't help myself
    primegits = []
    base = 2
    while num > 0:
        primegits.append(num % base)
        num //= base
        base = nextprime(base)
    return tuple(primegits)


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


def prime_residues(num, i):
    residues = []
    for k in range(1, i + 1):
        residues.append(num % prime(k))
    return tuple(residues)


def prime_residues_inverse(residues):
    moduli = [prime(i) for i in range(1, len(residues) + 1)]
    value, _ = crt(moduli, residues, check=False)
    return value


def full_prime_residues(num):
    return prime_residues(num, primepi(num))

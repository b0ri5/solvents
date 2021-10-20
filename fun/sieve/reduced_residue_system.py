# See https://en.wikipedia.org/wiki/Reduced_residue_system

from functools import cache
from math import gcd
from sympy import isprime, prime, primorial


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


# The elements that the residue r in rss(i) contributes from rss(i + 1) 
def descendants(r, i):
  primorial_i = primorial(i)
  next_prime = prime(i + 1)
  for k in range(0, next_prime):
    candidate = primorial_i * k + r
    if candidate % next_prime != 0:
      yield candidate


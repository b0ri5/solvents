# See https://en.wikipedia.org/wiki/Reduced_residue_system

from functools import cache
from math import gcd
from sympy import prime, primorial


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
  
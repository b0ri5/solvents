# See https://en.wikipedia.org/wiki/Reduced_residue_system

import random

from collections import deque, namedtuple
from functools import cache
from math import gcd
from itertools import count
from sympy.ntheory.modular import crt
from sympy import isprime, nextprime, prevprime, primepi, primerange

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


def reduced_residue_system_primorial(i):
    if i == 1:
        yield 1
        return
    for residue in reduced_residue_system_primorial(i - 1):
        for child in children(residue, i - 1):
            yield child


def reduced_residue_system_primorial_new(i):
    """
    Like reduced_residue_system_primorial(i) but only only yields elements not
    in reduced_residue_system_primorial(i - 1).
    """
    if i == 1:
        yield 1
        return
    for residue in reduced_residue_system_primorial(i - 1):
        for child in children(residue, i - 1):
            if child != residue:
                yield child


def all_reduced_residue_system_primorial():
    """
    Iterates through all unique elements of all primorial reduced residue systems.
    Each residue is returned only for the first system it is a member of.

    Yields tuples (r, i) where r is the residue and i is the system it is first seen in.
    """
    for i in count(start=1):
        for residue in reduced_residue_system_primorial_new(i):
            yield (residue, i)


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


def parent(residue):
    return primoradic_to_int(primoradic(residue)[:-1])


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
    min_child = None
    min_i = None
    while not min_child:
        residue, i = queue.pop()
        for child in children(residue, i):
            if isprime(child):
                min_child = child
                min_i = i + 1
                break
            else:
                queue.appendleft((child, i + 1))

    # Consume the rest of the queue to get the minimum
    while queue:
        residue, i = queue.pop()
        for child in children(residue, i):
            if child < min_child and isprime(child):
                min_child = child

    return min_child, min_i


def min_prime_descendant_simple(residue, i):
    primorial_i = primorial(i)
    for k in count():
        num = residue + k * primorial_i
        if isprime(num):
            return num


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


def primoradic_to_int(primegits):
    num = primegits[0]
    for i, primegit in enumerate(primegits[1:]):
        num += primegit * primorial(i + 1)
    return num


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


def min_composite(i):
    # There are no composites in rrsp(1..3)
    if i < 4:
        return None
    return prime(i + 1) * prime(i + 1)


def max_power_composite(i):
    if i < 4:
        return None
    low = 2
    high = i
    next_prime = prime(i + 1)
    primorial_i = primorial(i)
    while low <= high:
        mid = low + ((high - low) // 2)
        power = next_prime**mid
        if power < primorial_i:
            low = mid + 1
        elif power > primorial_i:
            high = mid - 1

    return next_prime**(low - 1)


def most_unique_factors_composite(i):
    if i < 4:
        return None
    next_prime = prime(i + 1)
    num = next_prime
    while num < primorial(i):
        next_prime = nextprime(next_prime)
        num *= next_prime
    return num // next_prime


def max_square_composite(i):
    if i < 4:
        return None
    sqrt = floor_sqrt(primorial(i))
    if isprime(sqrt):
        largest_prime_factor = sqrt
    else:
        largest_prime_factor = prevprime(sqrt)
    return largest_prime_factor**2


def max_consecutive_primes_composite(i):
    if i < 4:
        return None
    sqrt = floor_sqrt(primorial(i))
    if isprime(sqrt):
        largest_prime_factor = sqrt
    else:
        largest_prime_factor = prevprime(sqrt)
    second_largest_prime_factor = prevprime(largest_prime_factor)
    one_larger_prime_factor = nextprime(largest_prime_factor)
    if largest_prime_factor * one_larger_prime_factor < primorial(i):
        return largest_prime_factor * one_larger_prime_factor
    return largest_prime_factor * second_largest_prime_factor


def longest_prime_gap_composite(i):
    if i < 4:
        return None
    quotient = primorial(i) // prime(i + 1)
    if isprime(quotient):
        return quotient * prime(i + 1)
    return prevprime(quotient) * prime(i + 1)


def interesting_composites(i):
    if i < 4:
        return
    yield min_composite(i)
    yield max_power_composite(i)
    yield most_unique_factors_composite(i)
    yield max_square_composite(i)
    yield max_consecutive_primes_composite(i)
    yield longest_prime_gap_composite(i)


def floor_sqrt(num):
    # Determine the bounds
    low = 1
    for i in count(start=0):
        root = 2**i
        if root**2 > num:
            high = root
            break
        low = root

    # low**2 <= num and high**2 < num
    while low < high:
        # The "+ 1" favors reducing high to ensure low**2 <= num
        mid = low + ((high - low + 1) // 2)
        square = mid**2
        if square < num:
            low = mid
        elif square > num:
            high = mid - 1
        else:
            return mid

    return low


def random_rrsp(i):
    if i == 1:
        return 1
    residue = random_rrsp(i - 1)
    children_list = list(children(residue, i - 1))
    return random.choice(children_list)


def random_rrsp_prefer_composites(i):
    if i == 1:
        return 1
    residue = random_rrsp_prefer_composites(i - 1)
    children_list = list(children(residue, i - 1))
    composite_children = list(filter(is_composite, children_list))
    if composite_children:
        return random.choice(composite_children)
    return random.choice(children_list)


def random_rrsp_prefer_composite_grandchildren(i):
    if i == 1:
        return 1
    residue = random_rrsp_prefer_composites(i - 1)
    children_list = list(children(residue, i - 1))
    composite_children = list(filter(is_composite, children_list))

    def all_children_are_composite(child):
        return all(map(is_composite, children(child, i)))

    composite_grandchildren = list(
        filter(all_children_are_composite, composite_children))
    if composite_grandchildren:
        return random.choice(composite_grandchildren)
    if composite_children:
        return random.choice(composite_children)
    return random.choice(children_list)


def is_composite(num):
    return num != 1 and not isprime(num)


# Also include the residue
def ancestors(residue):
    primegits = primoradic(residue)
    ancestors_list = []
    for i in range(1, len(primegits) + 1):
        ancestors_list.append(primoradic_to_int(primegits[:i]))
    return tuple(ancestors_list)


def ancestors_compositeness(residue):
    return tuple(map(is_composite, ancestors(residue)))

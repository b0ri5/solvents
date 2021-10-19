from math import gcd
from itertools import islice
from sympy import isprime, prime, primorial, sieve

def is_twin_prime(n):
    return isprime(n) and isprime(n + 2)

import functools
import itertools


@functools.cache
def prime_gaps(prime_index):
    if prime_index == 2:
        return (3, (2,))
    prev_prime, prev_gaps = prime_gaps(prime_index - 1)
    next_prime = prev_prime + prev_gaps[0]
    # Rotate the previous gaps one to the left: [g1, g2, ...] -> [g2, ..., g1]
    prev_gaps = prev_gaps[1:] + (prev_gaps[0],)
    running_sum = next_prime
    new_gaps = []
    for gaps_index in range(prev_prime * len(prev_gaps)):
        prev_gap = prev_gaps[gaps_index % len(prev_gaps)]
        if running_sum % prev_prime == 0:
            new_gaps[-1] += prev_gap
        else:
            new_gaps.append(prev_gap)
        running_sum += prev_gap
    return (next_prime, tuple(new_gaps))


def apply_gaps(start, gaps):
    current = start
    for gap in itertools.cycle(gaps):
        yield current
        current += gap

def f2():
    seen_twins = [3]
    # num_twos is https://oeis.org/A059861
    print('num_twins', 'new_twins', 'num_primes', 'num_twos')
    for i in range(2, 12):
        prime, gaps = prime_gaps(i)
   #     print([k for k in range(1, primorial(i)) if gcd(k, primorial(i)) == 1])
  #      print(prime, gaps)
        #print(prime, len(gaps))
        candidates = list(islice(apply_gaps(prime, gaps), len(gaps) * prime))
        #print(list(candidates))
        twins = [p for p in candidates if is_twin_prime(p)]
 #       print(twins)
        new_twins = []
        for t in twins:
            if t not in seen_twins:
                seen_twins.append(t)
                new_twins.append(t)
        #print('twins ', twins)
        #print('seen_twins', seen_twins)
        #print('new_twins', new_twins)
        num_primes = sum(isprime(k) for k in candidates)
        num_twos = sum(g == 2 for g in prime_gaps(i + 1)[1])
        print(len(twins), len(new_twins), num_primes, num_twos)

def f3():
    seen_twins = [3]
    # num_twos is https://oeis.org/A059861
    print('num_twins', 'new_twins', 'num_primes', 'num_twos')
    for i in range(2, 8):
#        print(primorial(i))
        candidates = [k for k in range(1, primorial(i)) if gcd(k, primorial(i)) == 1]
        print(candidates)
        twins = [p for p in candidates if is_twin_prime(p)]
#        print(twins)
        new_twins = []
        for t in twins:
            if t not in seen_twins:
                seen_twins.append(t)
                new_twins.append(t)
        num_primes = sum(isprime(k) for k in candidates)
        twos = [((k + 2) % primorial(i)) in candidates for k in candidates]
        num_twos = sum(twos)
        print(len(twins), len(new_twins), num_primes, num_twos)

f2()
#f3()
#print([i for i in range(1, primorial(2)) if gcd(i, primorial(i)) == 1])


def f1():
    upcoming_twins = [3]
    for i in range(2, 100):
        p = prime(i)
        if not is_twin_prime(p):
            continue
        print(upcoming_twins)
        upcoming_twins.remove(p)
        print(p, primorial(i - 1))
        l = [p + primorial(i - 1) * k for k in range(1, p)]
        #print(l)
        twin_primes = []
        for k in l:
            if is_twin_prime(k):
                twin_primes.append(k)
                upcoming_twins.append(k)

        print(twin_primes)            
        #twin_primes = [is_twin_prime(k) for k in l]
        #print(twin_primes)
        print(len(twin_primes))
        primes = [isprime(k) for k in l]
        print(sum(primes))
        print()

# The zeroes are 137 and 149
# twin_prime
# 1, 3, 5, 2, 2, 2, 1, 2, 2, 0, 0, 2, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1
# primes
# 2, 4, 6, 8, 9, 12, 8, 9, 12, 5, 10, 11, 13, 12, 17, 8, 12, 14, 12, 12, 9, 11, 11, 14
# These are not in the OEIS.

# at index 1 we add 1
# then we remove one and add 3 so 3
# then remove one and add 5 so 7
# then 8, 9, 10, 10, 11, 12, 11, 10, 11, 11, 11, 11, 10, 9, 8, 7, 6

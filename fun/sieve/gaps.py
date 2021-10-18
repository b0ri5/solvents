import functools
import itertools


@functools.cache
def gaps(prime_index):
    if prime_index == 2:
        return (3, (2,))
    prev_prime, prev_gaps = gaps(prime_index - 1)
    next_prime = prev_prime + prev_gaps[0]
    # Rotate the previous gaps one to the right: [g1, g2, ...] -> [g2, ..., g1]
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

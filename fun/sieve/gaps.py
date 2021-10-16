import functools


@functools.cache
def gaps(n):
    if n == 2:
        return (3, (2,))
    prev_p, prev_gaps = gaps(n - 1)
    # Start at the next prime
    p = prev_p + prev_gaps[0]
    # Rotate the previous gaps one to the right: [g1, g2, ...] -> [g2, ..., g1]
    prev_gaps = prev_gaps[1:] + (prev_gaps[0],)
    # The running sum
    s = p
    # The new gaps
    g = []
    for idx in range(prev_p * len(prev_gaps)):
        prev_gap = prev_gaps[idx % len(prev_gaps)]
        if s % prev_p == 0:
            g[-1] += prev_gap
        else:
            g.append(prev_gap)
        s += prev_gap
    return (p, tuple(g))

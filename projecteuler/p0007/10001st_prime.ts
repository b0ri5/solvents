// This does an unbounded sieve
export const nthPrime = function (n: number): number {
  // A map from composite numbers to the prime factors that resulted in them being known-composite
  const composites = new Map<number, number[]>();
  const addComposite = function (composite: number, prime: number): void {
    let primes = composites.get(composite);
    if (!primes) {
      primes = [];
      composites.set(composite, primes);
    }
    primes.push(prime);
  };
  let latestPrime = 2;
  let numPrimes = 1;
  for (let i = 3; numPrimes < n; i += 2) {
    const primes = composites.get(i);
    if (primes) {
      for (const p of primes) {
        // We are skipping evens so ignore i + 2p next
        addComposite(i + 2 * p, p);
      }
      composites.delete(i);
    } else {
      numPrimes += 1;
      latestPrime = i;
      // The next multiple to check should not be divisible by
      // any smaller prime so check i*i next
      addComposite(i * i, i);
    }
  }
  return latestPrime;
};

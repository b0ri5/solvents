// Probably the simplest unbounded sieve
export const simplestPrimes = function* () {
  const composites = new Map<number, number[]>();
  const add = function (pq: number, p: number) {
    let ps = composites.get(pq);
    if (!ps) {
      ps = [];
      composites.set(pq, ps);
    }
    ps.push(p);
  };
  for (let i = 2; ; i++) {
    const ps = composites.get(i);
    if (ps) {
      for (const p of ps) {
        add(i + p, p);
      }
      composites.delete(i);
    } else {
      yield i;
      add(2 * i, i);
    }
  }
};

// Like simplestPrimes but uses a step size of two and initially
// adds the first composite to check as the square of the prime.
export const simplerPrimes = function* () {
  const composites = new Map<number, number[]>();
  const add = function (pq: number, p: number) {
    let ps = composites.get(pq);
    if (!ps) {
      ps = [];
      composites.set(pq, ps);
    }
    ps.push(p);
  };
  yield 2;
  for (let i = 3; ; i += 2) {
    const ps = composites.get(i);
    if (ps) {
      for (const p of ps) {
        add(i + 2 * p, p);
      }
      composites.delete(i);
    } else {
      yield i;
      add(i * i, i);
    }
  }
};

// Like simplerPrimes but when re-adding a composite for a prime,
// the composite will not be divisible by any smaller primes.
//
// The big difference here is that the map is from composite to a
// generator of the next composites to use.
export const primes = function* () {
  const composites = new Map<number, Generator<number>>();
  yield 2;
  const allPrimes = [];
  for (let i = 3; ; i += 2) {
    let gen = composites.get(i);
    if (gen) {
      composites.delete(i);
    } else {
      yield i;
      allPrimes.push(i);
      gen = multiplesOfPrimeNotDivisibleBySmallerPrimes(allPrimes, i);
    }
    composites.set(gen.next().value, gen);
  }
};


// This is a generator for all numbers which are multiples
// of a given prime but not divisible by smaller primes.
// For example, for 7 this will generate all numbers like
// 2^0 * 3^0 * 5^0 * 7n where n >= 7.
export function* multiplesOfPrimeNotDivisibleBySmallerPrimes(
  primes: number[],
  p: number
) {
  yield p * p;
  for (let i = p + 2; ; i += 2) {
    let isDivisibleBySmallerPrime = false;
    for (const q of primes) {
      if (q === p) {
        break;
      }
      if (i % q === 0) {
        isDivisibleBySmallerPrime = true;
        break;
      }
    }
    if (!isDivisibleBySmallerPrime) {
      yield p * i;
    }
  }
}

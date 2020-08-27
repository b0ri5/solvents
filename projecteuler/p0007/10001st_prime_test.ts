import {
  multiplesOfPrimeNotDivisibleBySmallerPrimes,
  primes,
  simplerPrimes,
  simplestPrimes,
} from './10001st_prime';

const nth = function (gen: Generator<number>, n: number) {
  for (let i = 0; i < n - 1; i++) {
    gen.next();
  }
  return gen.next().value;
};

describe('nth prime', () => {
  it('returns the nth prime', () => {
    expect(nth(primes(), 1)).toBe(2);
    expect(nth(primes(), 6)).toBe(13);
    expect(nth(primes(), 10001)).toBe(104743);
  });
});

describe('simplestPrimes', () => {
  it('generates primes', () => {
    const gen = simplestPrimes();
    expect(gen.next().value).toBe(2);
    expect(gen.next().value).toBe(3);
    expect(gen.next().value).toBe(5);
    expect(gen.next().value).toBe(7);
    expect(gen.next().value).toBe(11);
  });
});

describe('prime generators', () => {
  it('they agree for the first many primes', () => {
    const generators = [simplestPrimes(), simplerPrimes(), primes()];
    for (let i = 0; i < 20000; i++) {
      const p = generators[0].next().value;
      for (let j = 1; j < generators.length; j++) {
        const q = generators[j].next().value;
        expect(p).toBe(q);
      }
    }
  });
});

const firstN = function (gen: Generator<number>, n: number) {
  const a = [];
  for (let i = 0; i < n; i++) {
    a.push(gen.next().value);
  }
  return a;
};

describe('multiplesOfPrimeNotDivisibleBySmallerPrimes', () => {
  it('returns multiples of the prime not divisible by smaller primes', () => {
    const gen = multiplesOfPrimeNotDivisibleBySmallerPrimes([3, 5], 7);
    expect(firstN(gen, 8)).toEqual([
      7 * 7,
      7 * 11,
      7 * 13,
      7 * 17,
      7 * 19,
      7 * 23,
      7 * 29,
      7 * 31,
    ]);
  });
});

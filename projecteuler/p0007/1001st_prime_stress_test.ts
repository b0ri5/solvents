import {primes, simplerPrimes, simplestPrimes} from './10001st_prime';

const nth = function (gen: Generator<number>, n: number) {
  for (let i = 0; i < n - 1; i++) {
    gen.next();
  }
  return gen.next().value;
};

describe('prime generators', () => {
  it('they agree for the first many primes', () => {
    const generators = [simplestPrimes(), simplerPrimes(), primes()];
    for (let i = 0; i < 1_000_000; i++) {
      const p = generators[0].next().value;
      for (let j = 1; j < generators.length; j++) {
        const q = generators[j].next().value;
        expect(p).toBe(q);
      }
    }
  });
});

describe('primes', () => {
  it('can calculate a large prime', () => {
    expect(nth(primes(), 2_000_000)).toBe(32452843);
  });
});

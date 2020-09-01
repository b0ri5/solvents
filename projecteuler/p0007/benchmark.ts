import {add, complete, cycle, suite} from 'benny';
import {primes, simplerPrimes, simplestPrimes} from './10001st_prime';

const firstN = function (gen: Generator<number>, n: number) {
  const a: number[] = [];
  for (let i = 0; i < n; i++) {
    a.push(gen.next().value);
  }
  return a;
};

const options = {
  minSamples: 5,
  maxTime: 30,
};

suite(
  'sieves',
  add(
    'simplestPrimes',
    () => {
      firstN(simplestPrimes(), 20_000);
    },
    options
  ),
  add(
    'simplerPrimes',
    () => {
      firstN(simplerPrimes(), 20_000);
    },
    options
  ),
  add.only(
    'primes',
    () => {
      firstN(primes(), 500_000);
    },
    options
  ),
  cycle(),
  complete()
);

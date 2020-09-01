import {add, complete, cycle, save, suite} from 'benny';
import {primes, simplerPrimes, simplestPrimes} from './10001st_prime';

const consumeN = function (gen: Generator<number>, n: number) {
  for (let i = 0; i < n; i++) {
    gen.next().value;
  }
};

const options = {
  minSamples: 5,
  maxTime: 30,
};

const addPrimes = function (name: string, gen: Generator<number>) {
  return add(name, () => consumeN(gen, 2_000), options);
};

suite(
  'sieves',
  addPrimes('simplestPrimes', simplestPrimes()),
  addPrimes('simplerPrimes', simplerPrimes()),
  addPrimes('primes', primes()),
  cycle(),
  complete(),
  save({file: 'sieves', details: true})
);

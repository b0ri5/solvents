import {List, OrderedMap} from 'immutable';

const createCycle = function (primes: number[], p: number) {
  let remainders = List<number>();
  for (let i = 0; primes[i] != p; i++) {
    remainders = remainders.push(p % primes[i]);
  }
  let cycle = OrderedMap<List<number>, List<number>>();
  while (!cycle.has(remainders)) {
    let nextRemainders = List<number>();
    for (let i = 0; i < remainders.size; i++) {
      nextRemainders = nextRemainders.push((remainders.get(i) + 1) % primes[i]);
    }
    cycle = cycle.set(List(remainders), nextRemainders);
    remainders = nextRemainders;
  }
  return cycle;
};

const primes = [3, 5, 7, 11, 13, 17, 19];

console.log(JSON.stringify(createCycle(primes, 5)));
console.log(JSON.stringify(createCycle(primes, 7)));

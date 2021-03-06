import {List, OrderedMap} from 'immutable';

const createCycle = function (primes: number[], p: number) {
  let remainders = List<number>();
  for (let i = 0; primes[i] !== p; i++) {
    remainders = remainders.push(p % primes[i]);
  }
  let cycle = OrderedMap<List<number>, List<number>>();
  while (!cycle.has(remainders)) {
    let nextRemainders = List<number>();
    for (let i = 0; i < remainders.size; i++) {
      nextRemainders = nextRemainders.push(
        (remainders.get(i)! + 1) % primes[i]
      );
    }
    cycle = cycle.set(List(remainders), nextRemainders);
    remainders = nextRemainders;
  }
  return cycle;
};

const hasZero = function (remainders: List<number>) {
  for (let i = 0; i < remainders.size; i++) {
    if (remainders.get(i) === 0) {
      return true;
    }
  }
  return false;
};

const keysWithZero = function (cycle: OrderedMap<List<number>, List<number>>) {
  let cnt = 0;
  for (const k of cycle.keys()) {
    if (hasZero(k)) {
      cnt++;
    }
  }
  return cnt;
};

const calculateSteps = function (
  cycle: OrderedMap<List<number>, List<number>>
) {
  const firstRemainders = cycle.keySeq().first() as List<number>;
  let remainders = firstRemainders;
  let steps = List<number>();
  let k = 0;
  do {
    remainders = cycle.get(remainders)!;
    k++;
    while (hasZero(remainders)) {
      remainders = cycle.get(remainders)!;
      k++;
    }
    steps = steps.push(k);
    k = 0;
  } while (!remainders.equals(firstRemainders));
  return steps;
};

const primes = [2, 3, 5, 7, 11, 13, 17, 19, 23];

for (const p of [3, 5, 7, 11, 13, 17, 19]) {
  const cycle = createCycle(primes, p);
  // The cycle sizes here are the "primorials" which are like factorials
  // but using primes instead of all integers.
  console.log('cycle size ' + cycle.size);
  // The number of cycles containing a zero remainder is the cotoitent of the primorial
  // and produces this sequence https://oeis.org/A053144.
  console.log('keys with zero ' + keysWithZero(cycle));
  if (cycle.size < 100) {
    console.log(JSON.stringify(cycle));
  }
  const steps = calculateSteps(cycle);
  if (steps.size < 500) {
    console.log('steps: ' + JSON.stringify(steps));
  }
  // The number of steps is the the sequence https://oeis.org/A005867 which is
  // the toitent of the primorials
  console.log('num steps ' + steps.size);
  console.log();
}

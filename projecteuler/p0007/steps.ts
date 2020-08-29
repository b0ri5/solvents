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
      nextRemainders = nextRemainders.push((remainders.get(i) + 1) % primes[i]);
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
  let firstRemainders: List<number>;
  for (const k of cycle.keys()) {
    firstRemainders = k;
    break;
  }
  let steps = List<number>();
  let remainders = firstRemainders;
  let k = 0;
  do {
    remainders = cycle.get(remainders);
    k++;
    while (hasZero(remainders)) {
      remainders = cycle.get(remainders);
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
  console.log('cycle size ' + cycle.size);
  console.log('keys with zero ' + keysWithZero(cycle));
  if (cycle.size < 100) {
    console.log(JSON.stringify(cycle));
  }
  const steps = calculateSteps(cycle);
  if (steps.size < 500) {
    console.log('steps: ' + JSON.stringify(steps));
  }
  console.log('num steps ' + steps.size);
  console.log();
}

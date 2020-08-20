// We roll two standard six-sided dice. Find the probability of the following
// events, assuming that the outcomes of the rolls are independent:
// (a) The two dice show the same number.
// (b) The number that appears on the first die is larger than the number on the
//     second.
// (c) The sum of the dice is even.
// (d) The product of the dice is a perfect square.
const dieRollsOfLength: (n: number) => number[][] = function (n: number) {
  if (n === 0) {
    return [[]];
  }
  const dieRolls = [];
  const shorterRolls = dieRollsOfLength(n - 1);
  for (let i = 0; i < shorterRolls.length; i++) {
    for (let j = 1; j <= 6; j++) {
      const rolls = shorterRolls[i].slice(0);
      rolls.push(j);
      dieRolls.push(rolls);
    }
  }
  return dieRolls;
};

export const sampleSpace = dieRollsOfLength(2);

const predicateA = function (run: number[]) {
  return run[0] === run[1];
};

const predicateB = function (run: number[]) {
  return run[0] > run[1];
};

const predicateC = function (run: number[]) {
  return (run[0] + run[1]) % 2 === 0;
};

const isPerfectSquare = function (n: number) {
  const sqrtFloor = Math.floor(Math.sqrt(n));
  return sqrtFloor * sqrtFloor === n;
};

const predicateD = function (run: number[]) {
  return isPerfectSquare(run[0] * run[1]);
};

const probability = function (predicate: (sample: number[]) => boolean) {
  const events = sampleSpace.filter(predicate);
  return events.length / sampleSpace.length;
};

export const a = probability(predicateA);
export const b = probability(predicateB);
export const c = probability(predicateC);
export const d = probability(predicateD);

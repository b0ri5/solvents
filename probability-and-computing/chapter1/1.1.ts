// We flip a fair coin ten times. Find the probability of the following events.
// (a) The number of heads and the number of tails are equal.
// (b) There are more heads than tails.
// (c) The ith flip and the (11 - i)th flip are the same for i = 1, ..., 5
// (d) We flip at least four consecutive heads.
const coinTossesOfLength: (n: number) => string[] = function (n: number) {
  if (n === 0) {
    return [''];
  }
  const coinTosses = [];
  const shorterRuns = coinTossesOfLength(n - 1);
  for (let i = 0; i < shorterRuns.length; i++) {
    const run = shorterRuns[i];
    coinTosses.push('H' + run);
    coinTosses.push('T' + run);
  }
  return coinTosses;
};

export const sampleSpace = coinTossesOfLength(10);

const predicateA = function (run: string) {
  let numHeads = 0;
  let numTails = 0;
  for (let i = 0; i < run.length; i++) {
    if (run[i] === 'H') {
      numHeads += 1;
    } else if (run[i] === 'T') {
      numTails += 1;
    }
  }
  return numHeads === numTails;
};

const predicateB = function (run: string) {
  let numHeads = 0;
  let numTails = 0;
  for (let i = 0; i < run.length; i++) {
    if (run[i] === 'H') {
      numHeads += 1;
    } else if (run[i] === 'T') {
      numTails += 1;
    }
  }
  return numHeads > numTails;
};

const predicateC = function (run: string) {
  for (let i = 0; i < run.length; i++) {
    if (run[i] !== run[run.length - 1 - i]) {
      return false;
    }
  }
  return true;
};

const predicateD = function (run: string) {
  let consecutiveHeads = 0;
  for (let i = 0; i < run.length; i++) {
    if (run[i] === 'H') {
      consecutiveHeads += 1;
      if (consecutiveHeads === 4) {
        return true;
      }
    } else {
      consecutiveHeads = 0;
    }
  }
  return false;
};

const probability = function (predicate: (run: string) => boolean) {
  const events = sampleSpace.filter(predicate);
  return events.length / sampleSpace.length;
};

export const a = probability(predicateA);
export const b = probability(predicateB);
export const c = probability(predicateC);
export const d = probability(predicateD);

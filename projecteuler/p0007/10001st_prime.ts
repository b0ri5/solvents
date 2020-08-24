// This does an unbounded sieve
export const nthPrime = function (n: number): number {
  // Need a map from number to a list of numbers
  const multiples: {[multiple: number]: number[]} = {};
  // Create a helper since Javascript doesn't have great multimap or
  // defaultdict support.
  const addMultiple = function (multiple: number, prime: number): void {
    if (multiple in multiples) {
      multiples[multiple].push(prime);
    } else {
      multiples[multiple] = [prime];
    }
  };
  let latestPrime = 2;
  let numPrimes = 1;
  for (let i = 3; numPrimes < n; i += 2) {
    if (i in multiples) {
      for (const p of multiples[i]) {
        // We are skipping evens so ignore i + 2p next
        addMultiple(i + 2 * p, p);
      }
      delete multiples[i];
    } else {
      numPrimes += 1;
      latestPrime = i;
      // The next multiple to check should not be divisible by
      // any smaller prime so check i*i next
      addMultiple(i * i, i);
    }
  }
  return latestPrime;
};

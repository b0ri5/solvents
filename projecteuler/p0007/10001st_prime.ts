import PriorityQueue from 'ts-priority-queue';

type Entry = {
  multiple: number;
  prime: number;
}

export const nthPrime = function (n: number): number {
  // Keep a priority queue of upcoming multiples to ignore.
  const multiples: PriorityQueue<Entry> = new PriorityQueue({
    comparator: e => e.multiple,
  });
  let latestPrime = 2;
  let numPrimes = 1;
  for (let i = 3; numPrimes < n; i += 2) {
    const entry = multiples.peek();
    if (entry.multiple === i) {
      // Remove and re-add all entries whose multiple is i
    } else {
      numPrimes += 1;
      latestPrime = i;
    }
  }
  return latestPrime;
};

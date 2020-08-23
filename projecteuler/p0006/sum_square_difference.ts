const sumOfSquares = function (n: number) {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i * i;
  }
  return sum;
};

const squareOfSum = function (n: number) {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i;
  }
  return sum * sum;
};

export const bruteForce = function (n: number) {
  return squareOfSum(n) - sumOfSquares(n);
};

// See https://brilliant.org/wiki/sum-of-n-n2-or-n3
// In wolframalpha.com input
//   expand (n*(n+1)/2)**2 - (n*(n+1)(2n+1)/6)
// to get
//   n^4/4 + n^3/6 - n^2/4 - n/6
export const closedForm = function (n: number) {
  return n ** 4 / 4 + n ** 3 / 6 - n ** 2 / 4 - n / 6;
};

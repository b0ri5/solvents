export const gcd = function (a: number, b: number) {
  if (a > b) {
    [a, b] = [b, a];
  }
  while (b % a > 0) {
    [a, b] = [b % a, a];
  }
  return a;
};

export const lcm = function (a: number, b: number) {
  return a * b / gcd(a, b);
};

export const bruteForce = function (n: number) {
  let smallestMultiple = 1;
  for (let i = 2; i <= n; i++) {
    smallestMultiple = lcm(smallestMultiple, i);
  }
  return smallestMultiple;
};

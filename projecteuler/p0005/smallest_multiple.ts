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
  const c = gcd(a, b);
  return a * b / c;
};

export const bruteForce = function (n: number) {
  let smallestMultiple = 1;
  for (let i = 2; i <= n; i++) {
    smallestMultiple = lcm(smallestMultiple, i);
  }
  return smallestMultiple;
};

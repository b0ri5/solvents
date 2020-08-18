/**
 * Calculates the arithmetic sum of a sequence according to:
 * http://www.mathsisfun.com/algebra/sequences-sums-arithmetic.html
 */
const arithmetic_sum = function (a: number, d: number, n: number) {
  return (n / 2) * (2 * a + d * (n - 1));
};

/**
 * Calculates the sum of the divisors {b, c} in range (1, upper)
 */
export const sum_divisors = function (
  upper: number,
  div1: number,
  div2: number
) {
  // The range is exclusive, so subtract 1 to get the inclusive upperbound
  const upper_inclusive = upper - 1;
  // Need the combo of div1 * div2 to subtract divisor double-counts
  const c_div = div1 * div2;

  return (
    arithmetic_sum(div1, div1, Math.floor(upper_inclusive / div1)) +
    arithmetic_sum(div2, div2, Math.floor(upper_inclusive / div2)) -
    arithmetic_sum(c_div, c_div, Math.floor(upper_inclusive / c_div))
  );
};

export const brute_force = function (n: number) {
  let sum = 0;
  for (let i = 0; i < n; i++) {
    if (i % 3 === 0 || i % 5 === 0) {
      sum += i;
    }
  }
  return sum;
};

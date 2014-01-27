'use strict';


/**
 * Calculates the arithmetic sum of a sequence according to:
 * http://www.mathsisfun.com/algebra/sequences-sums-arithmetic.html
 *
 * @param {number} a The first term
 * @param {number} d The "common difference" or step between numbers
 * @param {number} n The number of terms in the sequence to sum
 * @return {number} The arithmetic sum of the sequence defined by a, d, and n
 */
const arithmetic_sum = function(a, d, n) {
  return (n / 2) * (2 * a + d * (n - 1));
};


/**
 * Calculates the sum of the divisors {b, c} in range (1, upper)
 * @param {number} upper The upperbound of the range to sum (1, upper)
 * @param {number} div1 The first divisor
 * @param {number} div2 The second divisor
 * @return {number} The sum of the multiples
 */
const sum_divisors = function(upper, div1, div2) {
  // The range is exclusive, so subtract 1 to get the inclusive upperbound
  const upper_inclusive = upper - 1;
  // Need the combo of div1 * div2 to subtract divisor double-counts
  const c_div = div1 * div2;

  return arithmetic_sum(div1, div1, Math.floor((upper_inclusive) / div1)) +
      arithmetic_sum(div2, div2, Math.floor((upper_inclusive) / div2)) -
      arithmetic_sum(c_div, c_div, Math.floor((upper_inclusive) / c_div));
};

exports.sum_divisors = sum_divisors;

'use strict';

// param a is the first term
// param r is the "common ratio" or step between numbers
// param n is the number of terms to sum
const geometric_sum = function(a, r, n) {
  return a * ((1 - Math.pow(r, n)) / (1 - r));
};

// param a defines the top of the range to sum (1, a)
// param b is the first divisor
// param c is the second divisor
const sum_divisors = function(a, b, c) {
  var bc = b * c;
  // Get the count of b, c, and b*c multiples in (1, a)
  var count_b = Math.floor((a - 1) / b);
  var count_c = Math.floor((a - 1) / c);
  var count_bc = Math.floor((a - 1) / bc);

  // Get the sum of b, c, and b*c
  var sum = geometric_sum(b, b, count_b);
  sum += geometric_sum(c, c, count_c);
  // Subtract b*c since we've double-counted it
  sum -= geometric_sum(bc, bc, count_bc);

  return sum;
};

exports.sum_divisors = sum_divisors;

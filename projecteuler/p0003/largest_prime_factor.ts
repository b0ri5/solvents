import BigNumber from 'bignumber.js';

BigNumber.config({
  DECIMAL_PLACES: 0,
  ROUNDING_MODE: BigNumber.ROUND_FLOOR,
});

export const largestPrimeFactor = function (n: BigNumber) {
  while (n.modulo(2).isEqualTo(0)) {
    n = n.dividedBy(2);
  }
  let largestPrimeFactor = 2;
  let sqrtn = n.squareRoot();
  for (let i = 3; sqrtn.isGreaterThanOrEqualTo(i); i += 2) {
    if (n.modulo(i).isEqualTo(0)) {
      do {
        n = n.dividedBy(i);
      } while (n.modulo(i).isEqualTo(0));
      largestPrimeFactor = i;
      sqrtn = n.squareRoot();
    }
  }
  if (n.isEqualTo(1)) {
    return largestPrimeFactor;
  }
  return n.toNumber();
};

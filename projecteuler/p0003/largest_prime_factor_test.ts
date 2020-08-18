import {largestPrimeFactor} from './largest_prime_factor';
import BigNumber from 'bignumber.js';

describe('largest_prime_factor', () => {
  it('should solve small input', () => {
    expect(largestPrimeFactor(new BigNumber(13195))).toBe(29);
  });
  it('should solve large input', () => {
    expect(largestPrimeFactor(new BigNumber('600851475143'))).toBe(6857);
  });
});

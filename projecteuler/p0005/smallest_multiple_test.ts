import {bruteForce, gcd, lcm} from './smallest_multiple';

describe('lcm', () => {
  it('should be the least common multiple', () => {
    expect(lcm(1, 1)).toBe(1);
    expect(lcm(1, 2)).toBe(2);
    expect(lcm(2, 3)).toBe(6);
    expect(lcm(6, 4)).toBe(12);
  });
});

describe('gcd', () => {
  it('should be the greatest common divisor', () => {
    expect(gcd(4, 6)).toBe(2);
    expect(gcd(6, 4)).toBe(2);
  });
});

describe('bruteForce', () => {
  it('should solve small input', () => {
    expect(bruteForce(10)).toBe(2520);
  });
  it('should solve large input', () => {
    expect(bruteForce(20)).toBe(232792560);
  });
});

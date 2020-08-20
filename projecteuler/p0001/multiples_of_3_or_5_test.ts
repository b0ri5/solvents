import {brute_force, sum_divisors} from './multiples_of_3_or_5';

describe('#sum_divisors()', () => {
  it('should be exclusive', () => {
    expect(sum_divisors(3, 3, 5)).toBe(0);
    expect(sum_divisors(4, 3, 5)).toBe(3);
    expect(sum_divisors(5, 3, 5)).toBe(3);
    expect(sum_divisors(6, 3, 5)).toBe(8);
  });
  it('should solve small example', () => {
    expect(sum_divisors(10, 3, 5)).toBe(23);
  });
  it('should solve large problem', () => {
    expect(sum_divisors(1000, 3, 5)).toBe(233168);
  });
});
describe('#brute_force()', () => {
  it('should be exclusive', () => {
    expect(brute_force(3)).toBe(0);
    expect(brute_force(4)).toBe(3);
    expect(brute_force(5)).toBe(3);
    expect(brute_force(6)).toBe(8);
  });
  it('should solve small example', () => {
    expect(brute_force(10)).toBe(23);
  });
  it('should solve large problem', () => {
    expect(brute_force(1000)).toBe(233168);
  });
});

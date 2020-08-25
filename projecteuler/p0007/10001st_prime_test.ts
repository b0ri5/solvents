import {nthPrime} from './10001st_prime';

describe('nthPrime', () => {
  it('returns the nth prime', () => {
    expect(nthPrime(1)).toBe(2);
    expect(nthPrime(6)).toBe(13);
    expect(nthPrime(10001)).toBe(104743);
    expect(nthPrime(1000000)).toBe(15485863);
  });
});

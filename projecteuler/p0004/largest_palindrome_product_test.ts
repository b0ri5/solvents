import {bruteForce} from './largest_palindrome_product';

describe('bruteForce', () => {
  it('should solve small input', () => {
    expect(bruteForce(2)).toBe(9009);
  });
  it('should solve large input', () => {
    expect(bruteForce(3)).toBe(906609);
  });
});

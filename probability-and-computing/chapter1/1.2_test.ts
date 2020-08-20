import {sampleSpace, a, b, c, d} from './1.2';

describe('1.2', () => {
  describe('sampleSpace', () => {
    it('has the expected size', () => {
      expect(sampleSpace.length).toBe(36);
    });
  });
  it('answers a', () => {
    // (a) The two dice show the same number.
    // So it's the diagonal of the 6x6 matrix, so 6/36
    expect(a).toBe(6 / 36);
  });
  it('answers b', () => {
    // (b) The number that appears on the first die is larger than the number
    // on the second.
    // Similar to 1.1b, subtract the diagonal and divide by 2, so (36 - 6) / 2
    expect(b).toBe(15 / 36);
  });
  it('answers c', () => {
    // (c) The sum of the dice is even.
    // An even plus an even is an even, and an odd plus and odd is an even.
    // So |{2, 4, 6}|^2 + |{1, 3, 5}|^2 = 18
    expect(c).toBe(18 / 36);
  });
  it('answers d', () => {
    // (d) The product of the dice is a perfect square.
    // The perfect squares less than or equal to 36 are
    // 1, 4, 9, 16, 25, and 36.
    // The diagonal gives us 6 matching samples.
    // And 16 = 2 * 8, so there are two more samples.
    expect(d).toBe(8 / 36);
  });
});

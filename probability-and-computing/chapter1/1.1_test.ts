import {sampleSpace, a, b, c, d} from './1.1';

describe('1.1', () => {
  describe('sampleSpace', () => {
    it('has the expected size', () => {
      expect(sampleSpace.length).toBe(1024);
    });
  });
  it('answers a', () => {
    // (a) The number of heads and the number of tails are equal.
    // So it's how many ways we can choose 5 heads (or tails) from 10
    // 10! / (5!5!) = 252
    expect(a).toBe(252 / 1024);
  });
  it('answers b', () => {
    // (b) There are more heads than tails.
    // This is the same as the number with less heads than tails.
    // So if we exclude all where the number of heads is the number of tails,
    // and divide by two we get the answer.
    expect(b).toBe((1024 - 252) / 2 / 1024);
  });
  it('answers c', () => {
    // (c) The ith flip and the (11 - i)th flip are the same for i = 1, ..., 5
    // This is the same as the number outcomes of flipping a coin 5 times.
    expect(c).toBe(32 / 1024);
  });
  it('answers d', () => {
    // (d) We flip at least four consecutive heads.
    // This is complicated. We simplify it by asking for how many samples
    // have at least four consecutive heads starting at a given position.
    // 0: HHHH****** so 2^6 = 64
    // 1: THHHH***** so 2^5 = 32
    // 2: *THHHH**** so 2^5 = 32
    // 3: **THHHH*** so 2^5 = 32
    // 4: ***THHHH** so 2^5 = 32
    // 5: [**** except HHHH]THHHH* so (2^4 - 1) * 2 = 30
    // 6: [***** except THHHH, HHHHT, or HHHHH]THHHH = 2^32 - 3 = 29
    // Summing gives 251.
    expect(d).toBe(251 / 1024);
  });
});

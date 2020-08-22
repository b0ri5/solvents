import {
  Deck,
  sampler,
  predicateA,
  predicateB,
  predicateC,
  predicateD,
} from './1.3';

type Sampler = () => Deck;
type Predicate = (deck: Deck) => boolean;

describe('1.3', () => {
  const pointsAfterDecimal = function (p: number) {
    let i = 0;
    while (p < 1) {
      p *= 10;
      i++;
    }
    return i;
  };
  describe('pointsAfterDecimal', () => {
    it('returns expected values', () => {
      expect(pointsAfterDecimal(0.5)).toBe(1);
      expect(pointsAfterDecimal(0.01)).toBe(2);
      expect(pointsAfterDecimal(0.000001)).toBe(6);
    });
  });
  const expectProbabilityConvergesTo = function (
    sampler: Sampler,
    filter: Predicate,
    p: number
  ) {
    let positiveSamples = 0;
    let numCloseConsecutiveSamples = 0;
    const precision = pointsAfterDecimal(p) + 2; // Be within 2 decimal points
    const maxSamples = 100000000;
    for (let numSamples = 1; numSamples <= maxSamples; numSamples++) {
      const sample = sampler();
      if (filter(sample)) {
        positiveSamples += 1;
      }
      const observedProbability = positiveSamples / numSamples;
      const difference = Math.abs(observedProbability - p);
      if (difference < Math.pow(0.1, precision) * p) {
        numCloseConsecutiveSamples += 1;
      } else {
        numCloseConsecutiveSamples = 0;
      }
      // We must have sampled at least 100 decks and been within precision
      // range for a proportion of the number of samples so far. These
      // numbers are tuned such that the test should run quickly but also
      // be fairly confident the predicate is converging.
      if (numSamples > 100 && numCloseConsecutiveSamples >= numSamples / 10) {
        expect(observedProbability).toBeCloseTo(p, precision);
        return;
      }
    }
    expect(positiveSamples / maxSamples).toBeCloseTo(p, precision);
  };
  describe('sampler', () => {
    it('generates a permutation of 0..51', () => {
      const cards = sampler();
      expect(cards.length).toBe(52);
      const seenCards: {[key: number]: boolean} = {};
      for (let i = 0; i < cards.length; i++) {
        seenCards[i] = true;
      }
      expect(Object.keys(seenCards).length).toBe(52);
    });
  });
  describe('predicateD', () => {
    it('should return true for full houses', () => {
      expect(predicateD([0, 13, 26, 1, 14])).toBe(true);
      expect(predicateD([0, 13, 39, 1, 14])).toBe(true);
      expect(predicateD([2, 13, 39, 1, 14])).toBe(false);
    });
  });
  describe('expectProbabilityConvergesTo', () => {
    it('should converge to 1 / 2', () => {
      const firstCardIsEven = function (cards: Deck) {
        return cards[0] % 2 === 0;
      };
      expectProbabilityConvergesTo(sampler, firstCardIsEven, 1 / 2);
    });
  });
  it('answers a', () => {
    // (a) The first two cards include at least one ace.
    // It's easier to look at the compliment, that there are no
    // aces in the first two cards.
    // The number of ways 2 cards can be permuted from 48,
    // then vary the rest.
    // 1 - (((48 permute 2) * 50!) / 52!)
    // 1 - 48!50! / 46!52!
    // 1 - (48 * 47) / (52 * 51)
    expectProbabilityConvergesTo(
      sampler,
      predicateA,
      1 - (48 * 47) / (52 * 51)
    );
  });
  it('answers b', () => {
    // (b) The first five cards include at least one ace.
    // This is similar to (a) but with five cards instead of two.
    // 1 - (((48 permute 5) * 47!) / 52!)
    // 1 - 48!47! / 43!52!
    // 1 - (47 * 46 * 45 * 44) / (52 * 51 * 50 * 49)
    expectProbabilityConvergesTo(
      sampler,
      predicateB,
      1 - (47 * 46 * 45 * 44) / (52 * 51 * 50 * 49)
    );
  });
  it('answers c', () => {
    // (c) The first two cards are a pair of the same rank.
    // Choose a rank, permute two of that rank, vary the rest.
    // ((13 choose 1) * (4 permute 2) * 50! / 52!)
    // (13 * 4!/2! * 50!) / 52!
    // (13 * 12) / (52 * 51)
    expectProbabilityConvergesTo(sampler, predicateC, (13 * 12) / (52 * 51));
  });
  it('answers d', () => {
    // (d) The first five cards form a full house.
    // Choose two ranks. Choose three of one, two of the other.
    // Permute the 5 cards. Then permute the rest.
    // ((13 choose 2) * (4 choose 3) * (4 choose 2) * 5! * 47!) / 52!
    // 13*12/2 * 4 * 12 * 120 / 52*51*50*49*48
    expectProbabilityConvergesTo(
      sampler,
      predicateD,
      (13 * 6 * 4 * 12 * 120) / (52 * 51 * 50 * 49 * 48)
    );
  });
});

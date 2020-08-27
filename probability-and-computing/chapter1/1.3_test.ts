import {
  Deck,
  Predicate,
  deck,
  predicateA,
  predicateB,
  predicateC,
  predicateD,
  shuffle,
} from './1.3';

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
    predicate: Predicate,
    p: number
  ) {
    let positiveSamples = 0;
    let numCloseConsecutiveSamples = 0;
    const precision = pointsAfterDecimal(p) + 2; // Be within a few decimal points
    const maxSamples = 10_000_000;
    for (let numSamples = 1; numSamples <= maxSamples; numSamples++) {
      shuffle(deck, predicate.numCardsUsed);
      if (predicate.predicate(deck)) {
        positiveSamples += 1;
      }
      const observedProbability = positiveSamples / numSamples;
      const difference = Math.abs(observedProbability - p);
      if (difference < Math.pow(0.1, precision) * p) {
        numCloseConsecutiveSamples += 1;
      } else {
        numCloseConsecutiveSamples = 0;
      }
      if (numCloseConsecutiveSamples >= 10) {
        expect(observedProbability).toBeCloseTo(p, precision);
        return;
      }
    }
    expect(positiveSamples / maxSamples).toBeCloseTo(p, precision);
  };
  describe('deck', () => {
    it('is a permutation of 0..51', () => {
      expect(deck.length).toBe(52);
      const seenCards = new Set();
      for (let i = 0; i < deck.length; i++) {
        seenCards.add(i);
      }
      expect(seenCards.size).toBe(52);
    });
  });
  describe('expectProbabilityConvergesTo', () => {
    it('should converge to 1 / 2', () => {
      const firstCardIsEven = {
        predicate: function (cards: Deck) {
          return cards[0] % 2 === 0;
        },
        numCardsUsed: 1,
      };
      expectProbabilityConvergesTo(firstCardIsEven, 1 / 2);
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
    expectProbabilityConvergesTo(predicateA, 1 - (48 * 47) / (52 * 51));
  });
  it('answers b', () => {
    // (b) The first five cards include at least one ace.
    // This is similar to (a) but with five cards instead of two.
    // 1 - (((48 permute 5) * 47!) / 52!)
    // 1 - 48!47! / 43!52!
    // 1 - (47 * 46 * 45 * 44) / (52 * 51 * 50 * 49)
    expectProbabilityConvergesTo(
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
    expectProbabilityConvergesTo(predicateC, (13 * 12) / (52 * 51));
  });
  describe('predicateD', () => {
    it('should return true for full houses', () => {
      expect(predicateD.predicate([0, 13, 26, 1, 14])).toBe(true);
      expect(predicateD.predicate([0, 13, 39, 1, 14])).toBe(true);
      expect(predicateD.predicate([2, 13, 39, 1, 14])).toBe(false);
    });
    it('answers d', () => {
      // (d) The first five cards form a full house.
      // Choose two ranks. Choose three of one, two of the other.
      // Permute the 5 cards. Then permute the rest.
      // ((13 choose 2) * (4 choose 3) * (4 choose 2) * 5! * 47!) / 52!
      // 13*12/2 * 4 * 12 * 120 / 52*51*50*49*48
      expectProbabilityConvergesTo(
        predicateD,
        (13 * 6 * 4 * 12 * 120) / (52 * 51 * 50 * 49 * 48)
      );
    });
  });
});

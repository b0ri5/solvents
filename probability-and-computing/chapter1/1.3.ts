// We shuffle a standard desk of cards, obtaining a permutation that is
// uniform over all 52! possible permutations. Find the probability of
// the following events.
// (a) The first two cards include at least one ace.
// (b) The first five cards include at least one ace.
// (c) The first two cards are a pair of the same rank.
// (d) The first five cards form a full house.

export type Deck = number[];

const shuffle = function (cards: Deck) {
  for (let i = 0; i < cards.length - 1; i++) {
    const k = Math.floor(Math.random() * (cards.length - i)) + i;
    [cards[i], cards[k]] = [cards[k], cards[i]];
  }
  return cards;
};

export const sampler = (function () {
  const cards = new Array(52);
  for (let i = 0; i < cards.length; i++) {
    cards[i] = i;
  }
  return function () {
    return shuffle(cards);
  };
})();

const rank = function (card: number) {
  return card % 13;
};

export const predicateA = function (cards: Deck) {
  return rank(cards[0]) === 12 || rank(cards[1]) === 12;
};

export const predicateB = function (cards: Deck) {
  for (let i = 0; i < 5; i++) {
    if (rank(cards[i]) === 12) {
      return true;
    }
  }
  return false;
};

export const predicateC = function (cards: Deck) {
  return rank(cards[0]) === rank(cards[1]);
};

export const predicateD = function (cards: Deck) {
  const rankCounts: {[key: number]: number} = {};
  for (let i = 0; i < 5; i++) {
    const cardRank = rank(cards[i]);
    rankCounts[cardRank] = rankCounts[cardRank] + 1 || 1;
    if (Object.keys(rankCounts).length > 2) {
      return false;
    }
    if (rankCounts[cardRank] === 4) {
      return false;
    }
  }
  return true;
};

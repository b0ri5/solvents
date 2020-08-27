// We shuffle a standard desk of cards, obtaining a permutation that is
// uniform over all 52! possible permutations. Find the probability of
// the following events.
// (a) The first two cards include at least one ace.
// (b) The first five cards include at least one ace.
// (c) The first two cards are a pair of the same rank.
// (d) The first five cards form a full house.

export type Deck = number[];

export const shuffle = function (cards: Deck, numCards: number) {
  for (let i = 0; i < numCards; i++) {
    const k = Math.floor(Math.random() * (cards.length - i)) + i;
    [cards[i], cards[k]] = [cards[k], cards[i]];
  }
  return cards;
};

export const deck = (function () {
  const cards = new Array(52);
  for (let i = 0; i < cards.length; i++) {
    cards[i] = i;
  }
  return cards;
})();

export type Predicate = {
  predicate: (deck: Deck) => boolean;
  // Knowing the number of cards used by the predicate allows for more efficient
  // sampling by only selecting a small number of cards, rather than shuffling the whole deck.
  numCardsUsed: number;
};

const rank = function (card: number) {
  return card % 13;
};

export const predicateA = {
  predicate: function (cards: Deck) {
    return rank(cards[0]) === 12 || rank(cards[1]) === 12;
  },
  numCardsUsed: 2,
};

export const predicateB = {
  predicate: function (cards: Deck) {
    for (let i = 0; i < 5; i++) {
      if (rank(cards[i]) === 12) {
        return true;
      }
    }
    return false;
  },
  numCardsUsed: 5,
};

export const predicateC = {
  predicate: function (cards: Deck) {
    return rank(cards[0]) === rank(cards[1]);
  },
  numCardsUsed: 2,
};

export const predicateD = {
  predicate: function (cards: Deck) {
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
  },
  numCardsUsed: 5,
};

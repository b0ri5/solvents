import {bruteForce, everyThird} from './even_fibonacci_numbers';

describe('even_fibonacci_numbers', () => {
  const solutions = {
    bruteForce: bruteForce,
    everyThird: everyThird,
  };
  const describeSolution = function (
    name: string,
    solution: (n: number) => number
  ) {
    describe(name, () => {
      it('should solve small input', () => {
        expect(solution(89)).toBe(44);
      });
      it('should solve large input', () => {
        expect(solution(4000000)).toBe(4613732);
      });
    });
  };
  describeSolution('bruteForce', bruteForce);
  describeSolution('everyThird', everyThird);
});

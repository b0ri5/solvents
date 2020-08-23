import {bruteForce, closedForm} from './sum_square_difference';

const solutions: Record<string, (n: number) => number> = {
  bruteForce: bruteForce,
  closedForm: closedForm,
};

for (const [name, solution] of Object.entries(solutions)) {
  describe(name, () => {
    it('should solve the small input', () => {
      expect(solution(10)).toBe(2640);
    });
    it('should solve the large input', () => {
      expect(solution(100)).toBe(25164150);
    });
  });
}

export const bruteForce = function (n: number) {
  let [a, b] = [1, 2];
  let sum = 0;
  do {
    if (b % 2 === 0) {
      sum += b;
    }
    [a, b] = [b, a + b];
  } while (b < n);
  return sum;
};

export const everyThird = function (n: number) {
  let [a, b] = [1, 2];
  let sum = 0;
  do {
    // Every third fibonacci number is even starting with 2
    // Odd + Even = Odd
    // Even + Odd = Odd
    // Odd + Odd = Even
    //
    // f_{n+1} = f_n + f_{n-1}
    // f_{n+2} = f_{n+1} + f_n
    //         = (f_n + f_{n-1}) + f_n
    //         = 2f_n + f_{n-1}
    // f_{n+3} = f_{n+2} + f_{n+1}
    //         = (2f_n + f_{n-1}) + (f_n + f_{n-1})
    //         = 3f_n + 2f_{n-1}
    sum += b;
    [a, b] = [2 * b + a, 3 * b + 2 * a];
  } while (b < n);
  return sum;
};

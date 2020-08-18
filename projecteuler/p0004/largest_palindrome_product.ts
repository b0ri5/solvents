const reverseDigits = function (n: number) {
  let reversed = 0;
  while (n > 0) {
    reversed *= 10;
    reversed += n % 10;
    n = Math.floor(n / 10);
  }
  return reversed;
};

export const bruteForce = function (numDigits: number) {
  const largest = Math.pow(10, numDigits) - 1;
  const smallest = Math.pow(10, numDigits - 1);
  let largestPalindrome = smallest + 1;
  for (let i = largest; i >= smallest; i--) {
    for (let j = largest; j >= i; j--) {
      const p = i * j;
      if (p > largestPalindrome && p === reverseDigits(p)) {
        largestPalindrome = p;
      }
    }
  }
  return largestPalindrome;
};

from itertools import count
from sympy import nextprime, prime, primorial


def main():
    all_num_factors = []
    all_products = []
    for i in range(1, 30):
        larger_prime = prime(i + 1)
        product = larger_prime
        num_factors = 0
        while product < primorial(i):
            num_factors += 1
            larger_prime = nextprime(larger_prime)
            product *= larger_prime

        all_num_factors.append(num_factors)
        all_products.append(product // larger_prime)
        print(i, num_factors, primorial(i), product // larger_prime)

    print(all_num_factors)
    print(all_products)


if __name__ == "__main__":
    main()

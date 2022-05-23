import math


def check_prime(number):
    for i in range(3, math.ceil(number ** (1 / 2)) + 1, 2):
        if number % i == 0:
            return False
    return True


def main():
    n = int(input())

    strongly_prime_numbers = [[2, 3, 5, 7]]
    numbers = [1, 3, 5, 7, 9]

    for i in range(1, n):
        strongly_prime_numbers.append([])
        for s in strongly_prime_numbers[i - 1]:
            for num in numbers:
                k = s * 10 + num
                if check_prime(k):
                    strongly_prime_numbers[i].append(k)

    for num in strongly_prime_numbers[n - 1]:
        print(num)


main()
from math import sqrt
# def isPrime(num):
#     flag = 0
#     if num > 1:
#         for i in range(2, int(sqrt(num)) + 1):
#             if num % i == 0:
#                 flag = 1
#                 break
#
#         if flag == 0:
#             print("Prime")
#         else:
#             print("Not Prime")
#     else:
#         print("Not Prime")
#
# isPrime(19)

# def intervalPrime(x, y):
#     prime_list = []
#     for i in range(x, y):
#         if i == 0 or i == 1:
#             continue
#         else:
#             for j in range(2, int(i/2) + 1):
#                 if i % j == 0:
#                     break
#                 else:
#                     prime_list.append(i)
#
#     print(prime_list)
#
#
# intervalPrime(2, 7)


def primes(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    print(prime_list)

primes(2, 7)

import sys
import math

argv = sys.argv[1:]

def is_prime(number):
    if number < 2:
        return False
    tmp = int(math.sqrt(number))
    for i in range(2, tmp + 1):
        if number % i == 0:
            return False
    return True

def print_results(number, results):
    to_print = ""
    counter = 1
    for i in range(len(results) - 1):
        if results[i] == results[i + 1]:
            counter += 1
        else:
            if counter > 1:
                to_print += str(results[i]) + "^" + str(counter) + "*"
            else:
                to_print += str(results[i]) + "*"
            counter = 1
    print(number, '=', to_print + str(results[-1]))
        

for i in argv:
    results = []
    number = int(i)
    original_number = number
    j = 2
    while j * j <= number:
        while number % j == 0 and is_prime(j):
            results.append(j)
            number //= j
        j += 1
    if number > 1:
        results.append(number)
    print_results(original_number, results)
    
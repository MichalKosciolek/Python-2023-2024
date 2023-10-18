def number_of_digits(number):
    counter = 0
    while number > 0:
        number //= 10
        counter += 1
    return counter

result = ""

cm = input()
cm = int(cm)

for i in "|...." * cm:
    result += i
result += "|\n0"

for i in range(1, cm + 1):
    result = result + (" " * int(5 - number_of_digits(i))) + str(i)

print(result)

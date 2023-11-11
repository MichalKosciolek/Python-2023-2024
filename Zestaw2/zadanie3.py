roman = input()

dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000}

roman = roman.upper()

def is_correct(roman):
    for i in range(len(roman)):
        if roman[i] not in dict:
            return False
        if i > 0 and dict[roman[i]] > dict[roman[i - 1]]:
            if roman[i - 1] not in ['I', 'X', 'C']:
                return False
            if (roman[i] == 'V' and roman[i - 1] != 'I') or (
                roman[i] == 'X' and roman[i - 1] != 'I') or (
                roman[i] == 'L' and roman[i - 1] != 'X') or (
                roman[i] == 'C' and roman[i - 1] != 'X') or (
                roman[i] == 'D' and roman[i - 1] != 'C') or (
                roman[i] == 'M' and roman[i - 1] != 'C'):
                return False
    return True

if not is_correct(roman):
    print("Wrong roman number")
    exit(0)

result = 0
for i in range(len(roman)):
    if i > 0 and dict[roman[i]] > dict[roman[i - 1]]:
        result += dict[roman[i]] - 2 * dict[roman[i - 1]]
    else:
        result += dict[roman[i]]

print(result)
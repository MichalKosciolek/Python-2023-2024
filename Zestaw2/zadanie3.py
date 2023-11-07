roman = input()

dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000}

roman = roman.upper()
    
result = 0
for i in range(len(roman)):
    if i > 0 and dict[roman[i]] > dict[roman[i - 1]]:
        result += dict[roman[i]] - 2 * dict[roman[i - 1]]
    else:
        result += dict[roman[i]]

print(result)
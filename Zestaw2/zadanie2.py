input = input()

words = 0
letters = 0
digits = 0
dict = {}

def is_punctation_mark(c):
    i = ord(c)
    if i >= ord('0') and i <= ord('9'):
        return 0
    if i >= ord('A') and i <= ord('Z') or i >= ord('a') and i <= ord('z'):
        return 1
    return 3

for i in range(len(input)):
    if is_punctation_mark(input[i]) == 0:
        digits += 1
        dict[input[i]] = dict[input[i]] + 1 if input[i] in dict else 1
    elif is_punctation_mark(input[i]) == 1:
        letters += 1
        dict[input[i]] = dict[input[i]] + 1 if input[i] in dict else 1
    
    if i == 0 and is_punctation_mark(input[i]) != 3:
        words += 1
    elif is_punctation_mark(input[i]) != 3 and is_punctation_mark(input[i - 1]) == 3:
        words += 1

print("Words: ", words)
print("Letters: ", letters)
print("Digits: ", digits)

for key, value in dict.items():
    print(key, ": ", value)
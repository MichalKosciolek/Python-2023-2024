S = input()

lower = []
upper = []
odd = []
even = []

for i in S:
    if i.islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
    elif i.isdigit():
        if int(i) % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

for i in sorted(lower):
    print(i, end='')
for i in sorted(upper):
    print(i, end='')
for i in sorted(odd):
    print(i, end='')
for i in sorted(even):
    print(i, end='')

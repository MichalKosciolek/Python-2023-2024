N = int(input())

def fun(N):
    max = 0
    counter = 0
    flag = False
    while N > 0:    
        if bin(N)[-1] == '0' and flag:
            counter += 1
        else:
            flag = True
            if counter > max:
                max = counter
            counter = 0
        N = N >> 1
    return max

print(fun(N))
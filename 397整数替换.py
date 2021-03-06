cnt = 0

def integerReplacement(n: int):
    global cnt
    if n == 1:
        return 0
    cnt += 1
    if n % 2 != 0:
        return 1 + min(integerReplacement(n+1), integerReplacement(n-1))
    else:
        return 1 + integerReplacement(n//2)

a = 1234
b = integerReplacement(a)
print(b)

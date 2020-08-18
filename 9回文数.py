def isPalindrome(x: int):
    if x < 0:
        return False
    if x != 0 and x % 10 == 0:
        return False
    reverted_number = 0               # 反转后一半的数字
    while x > reverted_number:
        reverted_number = reverted_number * 10 + x % 10
        x = x // 10
    return x == reverted_number or reverted_number // 10 == x

a = 123321
b = isPalindrome(a)
print(b)
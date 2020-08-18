class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == '0' and num2 == '0':
            return '0'
        n1 = len(num1)
        n2 = len(num2)
        res = [0 for _ in range(max(n1, n2)+1)]
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(min(n1, n2)):
            tmp = ord(num1[i])+ord(num2[i])-2*ord('0') + res[i]
            res[i] = tmp % 10
            res[i+1] = tmp // 10
        while i+1 <= n1-1:
            tmp = res[i+1] + ord(num1[i+1]) - ord('0')
            res[i+1] = tmp % 10
            res[i+2] = tmp // 10
            i += 1
        while i+1 <= n2-1:
            tmp = res[i+1] + ord(num2[i+1]) - ord('0')
            res[i+1] = tmp % 10
            res[i+2] = tmp // 10
            i += 1
        k = len(res) - 1
        while k >= 0 and res[k] == 0:
            k -= 1
        ans = ''
        while k >= 0:
            ans += str(res[k])
            k -= 1
        return ans

a = '584'
b = '18'
s = Solution()
c = s.addStrings(a, b)
print(c)
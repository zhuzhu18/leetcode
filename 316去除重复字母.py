from collections import Counter

def removeDuplicateLetters(s: str):
    stack = []
    counter = Counter(s)
    existed = set()
    for c in s:
        if c not in existed:
            while len(stack) > 0 and c < stack[-1] and counter[stack[-1]] > 0:
                tmp = stack.pop()        # 如果当前字母比栈顶字母小并且栈顶字母在后面的字符串中还出现过, 就弹出栈顶元素
                existed.remove(tmp)      # 移出栈顶元素的同时集合中也要删除该元素, 以避免后面的元素不会被添加进栈中
            stack.append(c)
            existed.add(c)       # existed始终与stack保持一致
        counter[c] -= 1
    return "".join(stack)

a = 'bcabc'
b = removeDuplicateLetters(a)
print(b)
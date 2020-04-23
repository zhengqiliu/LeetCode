class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        s = s.replace(' ', '')
        s += '+'
        num = 0
        symbol = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = int(s[i]) + 10*num
            else:
                if symbol == '+':
                    stack.append(num)
                elif symbol == '-':
                    stack.append(-num)
                elif symbol == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                symbol = s[i]
                num = 0
                
        return sum(stack)

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def transfer(s):
            stack = []
            for ch in s:
                if ch != '#':
                    stack.append(ch)
                else:
                    if stack:
                        stack.pop()
            
            return stack
        
        return transfer(S) == transfer(T)

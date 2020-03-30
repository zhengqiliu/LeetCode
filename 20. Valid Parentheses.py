class Solution:
    def isValid(self, s: str) -> bool:
        left = ['{', '[', '(']
        right = ['}', ']', ')']
        stack = []
        for ch in s:
            if ch in left:
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top not in left or right.index(ch) != left.index(top):
                    return False
        if stack:
            return False
        
        return True

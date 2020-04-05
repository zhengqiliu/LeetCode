class Solution:
    def simplifyPath(self, path: str) -> str:
        symbol = [s for s in path.split('/') if s!= '' and s != '.']
        stack = []
        for s in symbol:
            if s == '..':
                if len(stack) >= 1:
                    stack.pop()
            else:
                stack.append(s)
        
        return '/' + '/'.join(stack)

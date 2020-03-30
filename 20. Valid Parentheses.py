class Solution:
    def isValid(self, s: str) -> bool:
        dic={'(':')','{':'}','[':']'}
        stack =[]
        if not s:
            return(True)
        if len(s)%2 == 1:
            return(False)
        for ch in s:
            if ch in dic.keys():
                stack.append(ch)
            elif ch in dic.values():
                if stack==[] or ch != dic[stack.pop()]:
                    return(False)
        if stack==[]:
            return(True)
        else:
            return(False)

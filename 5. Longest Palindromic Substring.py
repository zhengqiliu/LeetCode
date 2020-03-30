class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            l = r = i
            while s[l] == s[r]:
                if r-l+1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
                if l<0 or r >=len(s):
                    break
                
        for i in range(len(s)-1):
            l, r = i, i+1
            while s[l] == s[r]:
                if r-l+1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
                if l<0 or r >=len(s):
                    break        
        
        return res
        

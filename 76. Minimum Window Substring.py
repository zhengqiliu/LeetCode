class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dicT = collections.Counter(t)
        dicS = collections.defaultdict(int)
        req = len(dicT)
        res = s + ' '
        l = r = 0
        while l<=r and r < len(s):
            dicS[s[r]] += 1
            if dicS[s[r]] == dicT[s[r]]:
                req -= 1
                while req == 0:
                    if r - l + 1 < len(res):
                        res = s[l:r+1]
                        
                    if dicS[s[l]] == dicT[s[l]]:
                        req += 1                    
                    dicS[s[l]] -= 1
                    l += 1

            r += 1
        return res if len(res) <= len(s) else ''

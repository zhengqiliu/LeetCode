class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def projector(s):
            res = ''
            seen = {}
            for ch in s:
                if ch not in seen:
                    seen[ch] = str(len(seen))
                res += seen[ch]
            
            return res
        
        return projector(s) == projector(t)

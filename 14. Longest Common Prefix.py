class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        common = strs[0]
        res = ""
        for i in range(len(common)):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or common[i] != strs[j][i]:
                    return res
            res += common[i]
        
        return res
            

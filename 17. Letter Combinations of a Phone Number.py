class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno",7:"pqrs", 8:"tuv", 9:"wxyz"}
        res = []
        def dfs(dig, path):
            if not dig:
                res.append(path)
                return
            chars = dic[int(dig[0])]
            for ch in chars:
                dfs(dig[1:], path + ch)
        dfs(digits, "")
        return res

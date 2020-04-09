class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = set()
        def dfs(index, path, s):
            if index == 4:
                if not s:
                    res.add(path[:-1])
                return
            for i in range(1,4):
                temp = s[:i]
                if not temp:
                    continue
                if len(temp) > 1 and temp[0] == '0':
                    continue
                if 0 <= int(temp) <= 255:
                    dfs(index+1, path + temp + '.', s[i:])
        
        dfs(0, '', s)
        
        return list(res)

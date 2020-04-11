class Solution:
    def grayCode(self, n: int) -> List[int]:
        visited = set()
        string = '0'*n
        res = []
        for _ in range(2**n):
            visited.add(string)
            res.append(string)
            for i in range(len(string)):
                if string[i] == '0':
                    new_string = string[:i] + '1' + string[i+1:]
                else:
                    new_string = string[:i] + '0' + string[i+1:]
                if new_string not in visited:
                    string = new_string
                    break
        
        def BtoD(b):
            res = 0
            index = 0
            for i in range(len(b)-1, -1, -1):
                res += int(b[i])*(2**index)
                index += 1
            return res
        
        for i in range(len(res)):
            res[i] = BtoD(res[i])
        
        return res
                
                
                
                
                
                
                

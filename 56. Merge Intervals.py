class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        times = []
        for item in intervals:
            times.append((item[0], -1))
            times.append((item[1], 1))
            
        times.sort()
        res = []
        cnt = 0
        start = 0
        for i in range(len(times)):
            if times[i][1] == -1:
                cnt += 1
                if cnt == 1:
                    start = times[i][0]
            else:
                cnt -= 1
                if cnt == 0:
                    res.append([start, times[i][0]])
                    
        for i in range(len(res)):
            if i > 0 and res[i-1][1] == res[i][0]:
                res = res[:i-1] + [[res[i-1][0], res[i][1]]]  + res[i+1:]
        
        return res

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def cnt(word):
            res = [0]*26
            for ch in word:
                res[ord(ch) - 97] += 1
            
            return tuple(res)
        
        count = collections.defaultdict(list)
        for s in strs:
            tupled_str = cnt(s)
            count[tupled_str].append(s)
        
        return [ans for ans in count.values()]

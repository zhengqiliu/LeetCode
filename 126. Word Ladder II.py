class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = set(wordList)
        if endWord not in words:
            return []
        layer = {}
        layer[beginWord] = [[beginWord]]
        while layer:
            new_layer = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    return layer[word]
                for i in range(len(word)):
                    for ch in 'qwertyuiopasdfghjklzxcvbnm':
                        new_word = word[:i] + ch + word[i+1:]
                        if new_word not in words:
                            continue
                        new_layer[new_word] += [j + [new_word] for j in layer[word]]
            words -= set(new_layer.keys())
            layer = new_layer
        
        return []
                
                
                
                
                
                

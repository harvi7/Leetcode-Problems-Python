class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        d = {}
        if len(sentence1) != len(sentence2):
            return False
        for i, val in enumerate(similarPairs):
            d.setdefault(val[0], set()).add(val[1])
            d.setdefault(val[1], set()).add(val[0]) 
    
        for wrd1, wrd2 in zip(sentence1, sentence2):
            if wrd1 == wrd2 or wrd2 in d.get(wrd1,[]) or wrd1 in d.get(wrd2,[]) :
                continue
            else:
                return False
                
        return True
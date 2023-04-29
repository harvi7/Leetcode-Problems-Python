class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False
        m = {}
        for p in similarPairs:
            parent1, parent2 = self.find(m, p[0]), self.find(m, p[1])
            if parent1 != parent2: m[parent1] = parent2

        for i in range(len(sentence1)):
            if sentence1[i] != sentence2[i] and self.find(m, sentence1[i]) != self.find(m, sentence2[i]): return False

        return True
    
    def find(self, m, s):
        if s not in m: m[s] = s
        return s if s == m[s] else self.find(m, m[s])
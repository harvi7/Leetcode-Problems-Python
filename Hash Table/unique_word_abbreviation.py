class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbrDict = collections.defaultdict(set)
        for s in dictionary: 
            abbr = self.toAbbr(s)
            self.abbrDict[abbr].add(s)

    def isUnique(self, word: str) -> bool:
        abbr = self.toAbbr(word)
        return self.abbrDict[abbr] <= {word}
    
    
    def toAbbr(self, s):
        n = len(s)
        if n <= 2:
            return s
        return s[0] + str(n - 2) + s[-1]
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        alphabet = string.ascii_lowercase
        min_dict = {c: 0 for c in alphabet}
        
        for ch, v in min_dict.items():
            min_dict[ch] = min([word.count(ch) for word in A])

        result = []
        for ch, count in min_dict.items():
            if count > 0:
                result += [ch] * count
        return result
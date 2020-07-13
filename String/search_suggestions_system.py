class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        lo, hi = 0, len(products)-1
        ans = []
        for i, letter in enumerate(searchWord):
            while lo < len(products) and (len(products[lo]) <= i or products[lo][i] != letter): lo += 1
            while hi >= 0 and (len(products[hi]) <= i or products[hi][i] != letter): hi -= 1
            ans.append(products[lo: min(lo + 3, hi + 1)])
        return ans
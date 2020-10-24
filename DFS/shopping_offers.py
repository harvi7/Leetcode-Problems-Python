# https://leetcode.com/problems/shopping-offers/discuss/487396/RZ-Top-down-solution-with-memoization-in-Python

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        if not price or not special or not needs:
            return 0
        return self.helper(price, special, needs, {})  
    
    def helper(self, price, special, needs, cache):
        needs = tuple(needs)
        if needs in cache:
            return cache[needs]
        
        n = len(needs)
        minPrice = sum(needs[i] * price[i] for i in range(n))
        
        for offer in special:
            if all(offer[i] <= needs[i] for i in range(n)):
                updatedNeeds = [needs[i] - offer[i] for i in range(n)]
                minPrice = min(minPrice, self.helper(price, special, updatedNeeds, cache) + offer[-1])
                
        cache[needs] = minPrice
        return minPrice
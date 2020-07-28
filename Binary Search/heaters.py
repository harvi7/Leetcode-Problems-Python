class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        heaters=[float('-inf')] + heaters + [float('inf')] 
        ans, i = 0, 0
        for house in houses:
            while house > heaters[i + 1]:  
                i +=1
            dis = min(house - heaters[i], heaters[i + 1]- house)
            ans = max(ans, dis)
        return ans
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        restaurants_1 = {u: i for i, u in enumerate(list1)}
        min_sum, res = 1e9, []
        
        for j, v in enumerate(list2):
            if v in restaurants_1.keys():
                temp_sum = j + restaurants_1[v]
                if temp_sum < min_sum:
                    res = [v]
                    min_sum = temp_sum
                elif temp_sum == min_sum:
                    res.append(v)
        return res
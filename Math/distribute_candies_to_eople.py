class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res, i, loops = [0] * num_people, 0, 0   
        while candies > 0:       
            if i == num_people:
                i = 0
                loops += 1
            
            currCandy = loops * num_people + (i + 1)
            if candies - currCandy < 0:
                res[i] += candies
            else:
                res[i] += currCandy
            i += 1
            candies -= currCandy         
        return res
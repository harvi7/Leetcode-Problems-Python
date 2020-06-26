class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if not points:
            return 0
        elif n <= 2:
            return n

        max_points = 0
        for i in range(n):
            slope_dict = {}
            same = 0
            a = points[i]
            for j in range(i + 1, n):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                if self.isSame(a, points[j]):
                    same += 1
                    continue
                gcd = self.generateGcd(x, y)
                x = x // gcd
                y = y // gcd
                slope = str(y) + "/" + str(x)
                slope_dict[slope] =  slope_dict.get(slope, 0) + 1
            localMax = 0
            for value in slope_dict.values():
                localMax = max(localMax, value)
            max_points = max(max_points, 1 + localMax + same)
        return max_points
    
    def isSame(self, a, b):
        return a[0] == b[0] and a[1] == b[1]

    def generateGcd(self, a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a
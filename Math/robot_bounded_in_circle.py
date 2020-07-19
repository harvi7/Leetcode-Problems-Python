class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, i, d = 0, 0, 0, [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for j in range(len(instructions)):
            if instructions[j] == 'R':
                i = (i + 1) % 4
            elif instructions[j] == 'L':
                i = (i + 3) % 4
            else:
                x += d[i][0]; y += d[i][1]

        return x == 0 and y == 0 or i > 0
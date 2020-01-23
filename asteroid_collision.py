class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            if not stack or asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                while True:
                    peek = stack[-1]
                    if peek < 0:
                        stack.append(asteroids[i])
                        break
                    elif peek == -asteroids[i]:
                        stack.pop()
                        break
                    elif peek > -asteroids[i]:
                        break
                    else:
                        stack.pop()
                        if not stack:
                            stack.append(asteroids[i])
                            break
        res = [None] * len(stack)
        for i in range(len(res) - 1, -1, -1):
            res[i] = stack.pop()
        return res
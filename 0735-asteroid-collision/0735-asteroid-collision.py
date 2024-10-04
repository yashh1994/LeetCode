class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for a in asteroids:
            while stk and stk[-1] > 0 and a < 0:
                if abs(stk[-1]) == abs(a):
                    stk.pop()
                    break
                elif abs(stk[-1]) < abs(a):
                    stk.pop()
                    continue
                elif abs(stk[-1]) > abs(a):
                    break
            else:
                stk.append(a)
        return stk

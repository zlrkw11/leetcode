class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []

        for ast in asteroids:
            if ast > 0:
                stk.append(ast)
            else:
                while stk and ast < 0 < stk[-1]:
                    if -ast > stk[-1]:
                        stk.pop()
                    elif -ast == stk[-1]:
                        stk.pop()
                        break
                    else:
                        break
                else:
                    stk.append(ast)
        
        return stk
            
        
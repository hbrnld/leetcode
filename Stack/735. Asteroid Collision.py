# https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for i in range(len(asteroids)):
            while stack and stack[-1] > 0 and asteroids[i] < 0:
                if stack[-1] + asteroids[i] < 0:
                    stack.pop()
                elif stack[-1] + asteroids[i] > 0:
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(asteroids[i])
        
        return stack
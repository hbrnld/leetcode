# https://leetcode.com/problems/daily-temperatures/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        output = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                output[index] = i - index
                print(f"output[{index}] = {i} - {index} = {output[index]}")
            stack.append(i)
        return output
    
temps = [73, 74, 75, 71, 69, 72, 76, 73]
s = Solution()
s.dailyTemperatures(temps)
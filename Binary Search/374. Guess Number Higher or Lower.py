# https://leetcode.com/problems/guess-number-higher-or-lower/description/?envType=study-plan-v2&envId=leetcode-75

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower, upper = 1, n
        
        while lower <= upper:
            current = (lower + upper) // 2
            status = guess(current)
            if status == 0:
                return current
            elif guess(current) == -1:
                upper = current - 1
            else: 
                lower = current + 1

def guess(input):
    solution = 9
    if input == solution:
        return 0
    elif input < solution:
        return 1
    else:
        return -1



        
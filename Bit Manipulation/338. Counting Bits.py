# https://leetcode.com/problems/counting-bits/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]quit
        """
        ans = [0] + [1]*n

        if n == 0:
            return ans

        for i in range(2, n+1):
            if i % 2 == 0:
                ans[i] = ans[i // 2]
            else:
                ans[i] = ans[i // 2] + 1
        return ans
    
    def countBitsOneLiner(self, n):
        return [sum(list(map(int, str(bin(i)[2:]).strip()))) for i in range(n+1)]
    
s = Solution()
print(s.countBits(7))
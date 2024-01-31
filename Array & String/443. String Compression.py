# https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0

        while i <= len(chars) - 1:
            count = 1
            j = 1

            # Iterate until no more same chars
            while i+j <= len(chars) - 1 and chars[i] == chars[i+j]:
                count += 1
                j += 1

            # Handle insertion depending on count
            if count == 1: 
                i += 1
            elif count < 10:
                chars[i+1] = str(count)
                del chars[i+2:i+j]
                i += 2
            else: 
                dts = list(str(count))
                chars[i+1:i+len(dts)] = dts
                del chars[i+len(dts)+1:i+j+1]
                i += len(dts) + 1

        return len(chars)
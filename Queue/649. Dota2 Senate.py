# https://leetcode.com/problems/dota2-senate/?envType=study-plan-v2&envId=leetcode-75

from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n = len(senate)
        qR = deque([i for i in range(n) if senate[i] == 'R'])
        qD = deque([i for i in range(n) if senate[i] == 'D'])

        while qR and qD: 
            # Compare the first from each party
            r = qR.popleft()
            d = qD.popleft()

            # Put winner at back of queue
            if r < d: 
                qR.append(n+r)
            else: 
                qD.append(n+d)
        
        return 'Radiant' if qR else 'Dire'
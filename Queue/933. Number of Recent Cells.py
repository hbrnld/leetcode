# https://leetcode.com/problems/number-of-recent-calls/description/?envType=study-plan-v2&envId=leetcode-75

from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        # Append new request
        self.queue.append(t)

        # Remove all requests outside specified interval
        while t - self.queue[0] > 3000:
            self.queue.popleft()
        
        # Return length of queue
        return len(self.queue)
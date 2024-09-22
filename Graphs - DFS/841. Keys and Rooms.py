# https://leetcode.com/problems/keys-and-rooms/description/?envType=study-plan-v2&envId=leetcode-75



class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        stack = [0]

        while stack:
            room = stack.pop()
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    stack.append(key)

        return len(visited) == len(rooms)
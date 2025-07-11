class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = rooms[0]
        s = {0,}
        while keys:
            key = keys.pop()
            if key not in s:
                s.add(key)
                keys += rooms[key]
        return len(s) == len(rooms)

        

# https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited_rooms = {0}
        rooms_to_visit = list(rooms[0])  # Make a deep copy.
        while rooms_to_visit:
            curr_room = rooms_to_visit.pop()
            if curr_room not in visited_rooms:
                visited_rooms.add(curr_room)
                rooms_to_visit.extend(rooms[curr_room])
        return len(visited_rooms) == len(rooms)

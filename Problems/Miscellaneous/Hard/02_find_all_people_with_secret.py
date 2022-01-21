# https://leetcode.com/problems/find-all-people-with-secret/

class DSU:
    def __init__(self, item_cnt: int):
        self.entries = [-1 for _ in range(item_cnt)]

    def _find(self, idx: int) -> int:
        seeker = idx
        while self.entries[seeker] >= 0:
            seeker = self.entries[seeker]
        representative, seeker = seeker, idx
        while seeker != representative:  # Path compression
            seeker_next = self.entries[seeker]
            self.entries[seeker] = representative
            seeker = seeker_next
        return representative

    def are_in_same_set(self, item_1: int, item_2: int) -> bool:
        representative_1 = self._find(item_1)
        representative_2 = self._find(item_2)
        return representative_1 == representative_2

    def union(self, item_1: int, item_2: int) -> None:
        if self.are_in_same_set(item_1, item_2):
            return
        representative_1 = self._find(item_1)
        representative_2 = self._find(item_2)
        size_1 = -self.entries[representative_1]
        size_2 = -self.entries[representative_2]
        new_size = size_1 + size_2
        if size_1 <= size_2:  # Merge set_1 into set_2
            self.entries[representative_2] = -new_size
            self.entries[representative_1] = representative_2
        else:  # Merge set_2 into set_1
            self.entries[representative_1] = -new_size
            self.entries[representative_2] = representative_1

    def reset_hack(self, item: int) -> None:
        # WARNING: This operation could lead to an invalid state!
        # Reset item to represent a set of size one, alone by itself.
        self.entries[item] = -1


class Solution:
    def findAllPeople(
            self, n: int, meetings: list[list[int]], firstPerson: int
    ) -> list[int]:
        dsu = DSU(n)
        owner_of_secret = 0  # According to problem statement.
        dsu.union(owner_of_secret, firstPerson)
        # Group meetings by time.
        meetings_by_time = dict()
        for person_1, person_2, time in meetings:
            meeting_parties = (person_1, person_2)
            if time not in meetings_by_time:
                meetings_by_time[time] = [meeting_parties]
            else:
                meetings_by_time[time].append(meeting_parties)
        # Check every time slot in increasing order.
        for curr_time in sorted(meetings_by_time.keys()):
            seen_people = set()
            # Connect everybody to the group of the owner of the
            # secret who learns the secret during the current time slot.
            for person_1, person_2 in meetings_by_time[curr_time]:
                dsu.union(person_1, person_2)
                seen_people.update({person_1, person_2})
            # We need to reset every group that is not connected to
            # the owner of the secret. There's no way to do this in
            # a traditional DSU, so we need a hacky solution.
            # Reset hack resets the given person to represent a lone set
            # of size one. The representative of such an entry will be
            # the index of the entry, which will always differ from the
            # representative of the owner of the secret.
            # So this hack may break some chains, but every entry that
            # points to such a lone set will eventually also get reset,
            # so at the end of the loop, the state of dsu will be valid.
            for person in seen_people:
                if not dsu.are_in_same_set(owner_of_secret, person):
                    dsu.reset_hack(person)
        # Now everybody who knows the secret shares the same group with
        # the owner of the secret. We just have to collect those people.
        secret_holders = list()
        for person in range(n):
            if dsu.are_in_same_set(owner_of_secret, person):
                secret_holders.append(person)
        return secret_holders

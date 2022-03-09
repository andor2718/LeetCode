# https://leetcode.com/problems/accounts-merge/

class DSU:
    def __init__(self, items: list[str]):
        self._entries = [-1 for _ in range(len(items))]
        self._item_to_idx = {
            item: idx for idx, item in enumerate(items)}

    def find_group_idx(self, item: str) -> int:
        seeker = idx = self._item_to_idx[item]
        while self._entries[seeker] >= 0:
            seeker = self._entries[seeker]
        group_idx, seeker = seeker, idx
        while seeker != group_idx:  # Path compression
            seeker_next = self._entries[seeker]
            self._entries[seeker] = group_idx
            seeker = seeker_next
        return group_idx

    def are_in_same_set(self, item_1: str, item_2: str) -> bool:
        group_idx_1 = self.find_group_idx(item_1)
        group_idx_2 = self.find_group_idx(item_2)
        return group_idx_1 == group_idx_2

    def union(self, item_1: str, item_2: str) -> None:
        if self.are_in_same_set(item_1, item_2):
            return
        group_idx_1 = self.find_group_idx(item_1)
        group_idx_2 = self.find_group_idx(item_2)
        size_1 = -self._entries[group_idx_1]
        size_2 = -self._entries[group_idx_2]
        new_size = size_1 + size_2
        if size_1 <= size_2:  # Merge set_1 into set_2
            self._entries[group_idx_2] = -new_size
            self._entries[group_idx_1] = group_idx_2
        else:  # Merge set_2 into set_1
            self._entries[group_idx_1] = -new_size
            self._entries[group_idx_2] = group_idx_1


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # Build a mail -> name lookup table.
        mail_to_name = dict()
        for account in accounts:
            name, mails = account[0], account[1:]
            for mail in mails:
                mail_to_name[mail] = name
        # Create a custom DSU with mails as keys.
        dsu = DSU(list(mail_to_name.keys()))
        # Find the union of all the mails belonging to the same account.
        for account in accounts:
            for i in range(2, len(account)):
                dsu.union(account[i - 1], account[i])
        # Create a list of mails for every group idx.
        group_idx_to_mails = dict()
        for mail in mail_to_name.keys():
            group_idx = dsu.find_group_idx(mail)
            if group_idx not in group_idx_to_mails:
                group_idx_to_mails[group_idx] = [mail]
            else:
                group_idx_to_mails[group_idx].append(mail)
        # Generate and return the result.
        result = list()
        for mails in group_idx_to_mails.values():
            mails.sort()
            name = mail_to_name[mails[0]]
            result.append([name] + mails)
        return result

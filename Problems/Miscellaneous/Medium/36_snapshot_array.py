# https://leetcode.com/problems/snapshot-array/

from collections import namedtuple

HistoryRecord = namedtuple('HistoryRecord', ['snap_id', 'value'])


class SnapshotArray:
    def __init__(self, length: int):
        self._curr_snap_id = 0
        self._histories = [
            [HistoryRecord(self._curr_snap_id, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        new_history_record = HistoryRecord(self._curr_snap_id, val)
        history_records = self._histories[index]
        last_record = history_records[-1]
        if last_record.snap_id == self._curr_snap_id:
            history_records[-1] = new_history_record
        else:
            history_records.append(new_history_record)

    def snap(self) -> int:
        self._curr_snap_id += 1
        return self._curr_snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        history_records = self._histories[index]
        max_idx = len(history_records) - 1
        low, high = 0, max_idx
        while True:
            mid = (low + high) // 2
            mid_record = history_records[mid]
            next_record = history_records[mid + 1] if mid != max_idx else None
            if mid_record.snap_id == snap_id:
                return mid_record.value
            elif mid_record.snap_id < snap_id:
                if not next_record or next_record.snap_id > snap_id:
                    return mid_record.value
                else:
                    low = mid + 1
            else:
                high = mid - 1

# https://leetcode.com/problems/number-of-provinces/

def reach_connected_cities(start_city_idx: int,
                           city_reached: list[bool],
                           isConnected: list[list[int]]) -> None:
    connected_cities = [start_city_idx]
    while connected_cities:
        city_idx = connected_cities.pop()
        city_reached[city_idx] = True
        for idx, is_connected in enumerate(isConnected[city_idx]):
            if is_connected and not city_reached[idx]:
                connected_cities.append(idx)


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        city_reached = [False for _ in range(n)]
        province_cnt = 0
        for idx in range(len(city_reached)):
            if not city_reached[idx]:
                province_cnt += 1
                reach_connected_cities(idx, city_reached, isConnected)
        return province_cnt

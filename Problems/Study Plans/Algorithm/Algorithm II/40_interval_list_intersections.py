# https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: list[list[int]],
                             secondList: list[list[int]]) -> list[list[int]]:
        result = list()
        while firstList and secondList:
            first_interval = firstList[0]
            second_interval = secondList[0]
            first_start, first_end = first_interval
            second_start, second_end = second_interval
            if first_start <= second_start:
                if second_start <= first_end:
                    intersection_start = second_start
                    intersection_end = min(first_end, second_end)
                    result.append([intersection_start, intersection_end])
                    if first_end < second_end:
                        firstList.pop(0)
                    elif second_end < first_end:
                        secondList.pop(0)
                    else:
                        firstList.pop(0)
                        secondList.pop(0)
                else:
                    firstList.pop(0)
            else:
                if first_start <= second_end:
                    intersection_start = first_start
                    intersection_end = min(first_end, second_end)
                    result.append([intersection_start, intersection_end])
                    if first_end < second_end:
                        firstList.pop(0)
                    elif second_end < first_end:
                        secondList.pop(0)
                    else:
                        firstList.pop(0)
                        secondList.pop(0)
                else:
                    secondList.pop(0)
        return result

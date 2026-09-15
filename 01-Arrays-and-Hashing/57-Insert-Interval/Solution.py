class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        def merge_intervals(interval_list: List[List[int]]) -> List[List[int]]:

            interval_list.sort()
            merged_result = [interval_list[0]]

            for start, end in interval_list[1:]:
                if merged_result[-1][1] < start:
                    merged_result.append([start, end])
                else:
                    merged_result[-1][1] = max(merged_result[-1][1], end)

            return merged_result

        intervals.append(newInterval)

        return merge_intervals(intervals)
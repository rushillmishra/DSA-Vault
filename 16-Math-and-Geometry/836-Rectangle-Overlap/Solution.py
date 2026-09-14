class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2

        # for x in range(x1, x2):
        #     for y in range(y1, y2):
        #         if x3 <= x < x4 and y3 <= y < y4:
        #             return True

        # return False

        intersect_width = max(0, min(x2, x4) - max(x1, x3))
        intersect_height = max(0, min(y2, y4) - max(y1, y3))

        return (intersect_width * intersect_height) > 0
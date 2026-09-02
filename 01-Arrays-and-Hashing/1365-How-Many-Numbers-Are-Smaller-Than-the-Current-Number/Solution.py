class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:

        n = len(nums)
        res = [0]*n
        for i in range(0, n):
            for j in range(0, n):
                if nums[j]<nums[i]:
                    res[i] += 1
        return res

solution = Solution()
print(solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
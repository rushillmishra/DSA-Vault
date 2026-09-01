class Solution:
    def countOdds(self, low: int, high: int) -> int:

        #Approach 1
        # count = 0
        # for i in range(low, high+1):
        #     if i%2==0:
        #         continue
        #     else:
        #         count = count + 1
        # return count

        #Approach 2
        return (high + 1) // 2 - low // 2
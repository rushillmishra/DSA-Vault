class Solution:
    def addDigits(self, num: int) -> int:

        #Approach 1
        # if num < 10:
        #     return num
        #
        # def addition(n):
        #     nsum = 0
        #     while n > 0:
        #         nsum = nsum + (n % 10)
        #         n = n // 10
        #
        #     return nsum
        #
        # while num >= 10:
        #     num = addition(num)
        #
        # return num

        # Approach 2
        # if num < 10:
        #     return num
        #
        # while num >= 10:
        #     nsum = 0
        #     while num > 0:
        #         nsum += num % 10
        #         num //= 10
        #     num = nsum
        #
        # return num

        #Approach 3
        return 0 if num==0 else 1+(num-1)%9
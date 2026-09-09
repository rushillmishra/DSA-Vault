class Solution:
    def countCommas(self, n: int) -> int:
        return n-999 if n>999 else 0
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(remain):
            if remain < 0:
                return -1
            if remain == 0:
                return 0
            min_ = 0

            for coin in coins:
                res = dp()
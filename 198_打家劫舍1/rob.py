class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        动态规划，dp存储以每个房子作为最后一个偷的房子偷到的最大金额，
        转移方程为：max(dp[i], 当前房间金额+dp[i-2]偷到的值)
        即，或者不偷当前房间，或者偷当前房间+隔1的房间
        """
        dp = [0]*len(nums)
        res = 0
        for i in range(len(nums)):
            if i == 0:
                dp[i] += nums[i]
                res = dp[i]
                continue        # 下一次循环
            if i > 1:
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            else:
                dp[i] = max(dp[i-1], nums[i])
            res = max(res, dp[i])

        return res

# O(N^2)
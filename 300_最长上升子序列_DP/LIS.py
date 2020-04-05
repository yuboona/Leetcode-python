from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return 1
        res = 0
        dp = [1 for i in range(length)]
        for i in range(1, length):
            # 计算以nums[i]为结尾的升序列
            j = 0
            while j < i:
                # 状态的转移
                if nums[j] < nums[i]:
                    # 严格小于，不可等于
                    dp[i] = max_(dp[j]+1, dp[i])
                j += 1
            if res < dp[i]:
                res = dp[i]

        return res


max_ = lambda x, y: x if x > y else y


max_ = lambda x, y: x if x > y else y


l = [1,3,6,7,9,4,10,5,6]
s = Solution()
s.lengthOfLIS(l)
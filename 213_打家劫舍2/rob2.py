from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        动态规划，dp存储以每个房子作为最后一个偷的房子偷到的最大金额，
        转移方程为：max(max_, 当前房间金额+不相邻的房子的值)
        """
        dp1 = [0]*len(nums)
        dp2 = [0]*len(nums)

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            # NOTE 注意边界条件，我的代码因为只处理length-1个值，所以不能处理length为1的nums[]
            return nums[0]

        res = 0
        # 不包括第一间房，但包括最后一间时的偷盗方式，用来找到，dp2[-1]
        for i in range(1, len(nums)):
            if i == 1:
                dp2[i] += nums[i]
                res = dp2[i]
                continue        # 下一次循环

            # 正常情况，注意这个2
            if i == 2:
                dp2[i] = max(dp2[i-1], nums[i])
            else:
                dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i])

        # 包括第一间，但不包括最后一间
        for i in range(len(nums)-1):
            if i == 0:
                dp1[i] += nums[i]
                res = dp1[i]
                continue        # 下一次循环

            # 正常情况，注意这个1
            if i == 1:
                dp1[i] = max(dp1[i-1], nums[i])
            else:
                dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
            res = max(res, dp1[i])

        res = max(res, dp2[-1])
        return res


s = Solution()
s.rob([1])
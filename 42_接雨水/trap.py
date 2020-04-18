from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        以积分的观点来看，只需关心每个i位置左右min(两个最高的柱子)-height；
        1、暴力法：O(N*N)，N次，每次要遍历N个来检查左右两边最高的两个柱子
        2、备忘录：O(2N)
        3、
        """
        # 备忘录法
        length = len(height)
        # 左边最高的
        dp_left = [0]*length
        dp_right = [0]*length

        for i in range(length):
            if i == 0:
                dp_left[i] = height[i]
                dp_right[-(1+i)] = height[-(1+i)]
            else:
                dp_left[i] = max(height[i], dp_left[i-1])
                dp_right[-(1+i)] = max(height[-(1+i)], dp_right[-(i)])

        res = 0
        for i in range(length):
            if min(dp_left[i], dp_right[i]) > height[i]:
                res += min(dp_left[i], dp_right[i]) - height[i]

        return res


s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))


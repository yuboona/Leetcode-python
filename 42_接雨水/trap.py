from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        以积分的观点来看，只需关心每个i位置左右min(两个最高的柱子)-height；
        1、暴力法：O(N*N)，N次，每次要遍历N个来检查左右两边最高的两个柱子
        2、备忘录：O(2N)
        3、双指针一次遍历法 O(N)：主要原理是，用积分法求积水时，对于两边的元素，我们双指针两端遍历时能
            分别得到左指针左边最高或右指针右边最高，当然这时还不能确定怎么积分当前的雨水，（因为还不能直到左指针右边的最高元素）
            但是没关系，我们只需要一个分类讨论！！分别按情况选择处理左指针还是处理右指针！！
            因为如果左指针左边最高小于右指针右边的最高，那么对于左边指针指向的元素来说，
            此时无论右边最高再往中间走的过程中还能高多少或者低多少，都不重要了，
            因为已经有一个r_max可以和这一元素左边的最高围起来一个水坑了
            同理，右指针的元素也是同样的情况
        """
        # # 备忘录法
        # length = len(height)
        # # 左边最高的
        # dp_left = [0]*length
        # dp_right = [0]*length

        # for i in range(length):
        #     if i == 0:
        #         dp_left[i] = height[i]
        #         dp_right[-(1+i)] = height[-(1+i)]
        #     else:
        #         dp_left[i] = max(height[i], dp_left[i-1])
        #         dp_right[-(1+i)] = max(height[-(1+i)], dp_right[-(i)])

        # res = 0
        # for i in range(length):
        #     if min(dp_left[i], dp_right[i]) > height[i]:
        #         res += min(dp_left[i], dp_right[i]) - height[i]

        # return res

        # 双指针
        length = len(height)
        left = 0
        right = length-1
        l_max = 0
        r_max = 0

        res = 0
        # 注意这个 <= 号，这个才能保证所有元素遍历一遍
        while left <= right:
            if l_max < r_max:
                # 注意这个max(,0)，因为不会出现*负雨水*
                res += max(l_max-height[left], 0)
                l_max = max(l_max, height[left])
                left += 1
            else:
                res += max(r_max-height[right], 0)
                r_max = max(r_max, height[right])
                right -= 1

        return res



s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))


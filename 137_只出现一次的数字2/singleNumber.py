from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        数学方法
        """
        keys = set([])
        sum1 = 0
        for i in nums:
            keys.add(i)
            sum1 += i
        sum2 = 0
        for i in keys:
            sum2 += i

        out = (sum2*3 - sum1) / 2
        return int(out)
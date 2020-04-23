# TODO 复杂度低的方法
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        暴力法：排序后，一一比较
        """
        sort_list = [i for i in nums]
        sort_list.sort()
        length = len(nums)
        res = []
        start = length
        end = 0
        for i in range(length):
            if sort_list[i] != nums[i]:
                start = min(start, i)
                end = max(end, i)
            else:
                pass
        if start-end == length:
            return 0
        else:
            return end-start+1
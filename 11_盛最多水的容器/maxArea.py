class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        暴力法:超时
        """
        '''
        length = len(height)
        max_ = 0
        for i in range(length):
            for j in range(i+1, length):
                cap = (j-i)*min(height[i], height[j]) 
                max_ = max(cap, max_)
        return max_
        '''
        """
        双指针
        """
        length = len(height)
        i = 0
        j = length-1
        max_ = 0
        while i<j:
            if height[i] > height[j]:
                area = height[j]*(j-i)
                j -= 1
                if max_ < area:
                    max_ = area
            else:
                area = height[i]*(j-i)
                i += 1
                if max_ < area:
                    max_ = area
        return max_
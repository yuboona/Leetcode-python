class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        暴力法
        """
        len1 = len(nums1)
        len2 = len(nums2)
        res = [0]*(len1+len2)
        
        i = 0
        j = 0 
        while i < len1 or j < len2:
            if i < len1 and j < len2 and  nums1[i] < nums2[j]:
                res[i+j] = nums1[i]
                i += 1
            elif i < len1 and j < len2:
                res[i+j] = nums2[j]
                j += 1
            elif i >= len1:
                res[i+j] = nums2[j]
                j += 1
            elif j >= len2:
                res[i+j] = nums1[i]
                i += 1

        if (len1+len2)%2 == 0:
            left = (len1+len2)/2 -1
            right = (len1+len2)/2
            return (res[int(left)]+res[int(right)])/2
        else:
            return res[int((len1+len2)/2)]


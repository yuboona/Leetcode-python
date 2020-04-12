class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """暴力法:双指针
        """
        len1 = len(haystack)
        len2 = len(needle)
        if len1 == '':
            return -1

        for i in range(len1-len2+1):
            visited = 0     # visited必须是每轮更新
            for j in range(len2):
                if haystack[i+j] != needle[j]:
                    visited = 1
                    break
            if(not visited and j == len2-1):
                return i
            visited = 0
        return -1

        # TODO 动态规划法



s = Solution()
s.strStr('hello', 'll')

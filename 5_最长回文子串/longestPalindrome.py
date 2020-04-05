class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        1. 动态规划
            - 发现有转移方程
            - 找到最基础的状态
            - 写出循环迭代
        """
        length = len(s)
        start = 0
        end = 0
        max_ = 0
        if length == 1:
            return s
        if length == 2:
            if s[0] == s[1]:
                return s
        # # #    dp矩阵
        #
        #
        # 注意浅拷贝的问题，直接[]对象*length，是浅拷贝
        dp = [[0]*length for i in range(length)]
        # 初始化部分基础状态
        for i in range(length):
            dp[i][i] = 1
            start = i
            end = i
        for i in range(0, length-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 2
                start = i
                end = i+1
        for j in range(2, length):
            # 范围是[2,length],不然[3,lenght]三个字母的串，就不能进行以下判断了
            for i in range(length):
                if i+j < length:
                    if s[i] == s[i+j] and dp[i+1][i+j-1]>0:
                        dp[i][i+j] = dp[i+1][i+j-1] + 2
                        if max_ < dp[i][i+j]:
                            max_ = dp[i][i+j]
                            start = i
                            end = i+j
                    else:
                        dp[i][i+j] = 0

        return s[start:end+1]



# s = Solution()
# s = s.longestPalindrome("babad")
# print(s)
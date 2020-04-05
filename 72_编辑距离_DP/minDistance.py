class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """动态规划解法
        1. 转移方程：
            - min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
            - 或者 min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
        2. 基础状态：
            - [0,0]，或，[0,i]，[i,0]。作为转移的起点
        3. for for 双层循环，覆盖所有状态

        """
        len1 = len(word1)
        len2 = len(word2)
        dp = [[0]*(len2+1) for _ in range(len1+1)]

        for i in range(len1+1):
            dp[i][0] = i
        for j in range(len2+1):
            dp[0][j] = j
        
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
        min_ = dp[len1][len2]
        return min_
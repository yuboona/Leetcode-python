import time


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """简单版，只求公共序列的**长度**
        """
        len1 = len(text1)
        len2 = len(text2)
        dp = [[0]*(len2+1) for _ in range(len1+1)]

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[i][j]

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        """复杂版，求公共序列的**具体**
            1. 迭代版
        """
        len1 = len(text1)
        len2 = len(text2)
        dp = [[0]*(len2+1) for _ in range(len1+1)]
        dp_str = [['']*(len2+1) for _ in range(len1+1)]

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    dp_str[i][j] = dp_str[i-1][j-1] + text1[i-1]
                elif dp[i][j-1] > dp[i-1][j]:
                    dp[i][j] = dp[i][j-1]
                    dp_str[i][j] = dp_str[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
                    dp_str[i][j] = dp_str[i-1][j]
        return dp_str[i][j]

    def longestCommonSubsequence3(self, text1: str, text2: str) -> int:
        """复杂版，求公共序列的**具体**
            2. 递归版：**其实可以不传递字符串的，需要使用闭包函数**
        """
        len1 = len(text1)
        len2 = len(text2)
        if len1 == 0 or len2 == 0:
            return ''

        if text1[-1] == text2[-1]:
            return self.longestCommonSubsequence3(text1[:-1], text2[:-1])+text1[-1]
        elif len(self.longestCommonSubsequence3(text1[:], text2[:-1])) > len(self.longestCommonSubsequence3(text1[:-1], text2[:])):
            return self.longestCommonSubsequence3(text1[:], text2[:-1])
        else:
            return self.longestCommonSubsequence3(text1[:-1], text2[:])

    def longestCommonSubsequence4(self, text1: str, text2: str) -> int:
        """复杂版，求公共序列的**具体**
            3. 递归版闭包版：**其实可以不传递字符串的，需要使用闭包函数**
        """
        len1 = len(text1)
        len2 = len(text2)

        def dp(i, j):
            """用i, j来指定位置
            """
            if i == 0 or j == 0:
                return ''
            if text1[i] == text2[j]:
                return dp(i-1, j-1) + text1[i]
            else:
                return dp(i, j-1) if len(dp(i, j-1)) > len(dp(i-1, j)) else dp(i-1, j)
        return dp(len1-1, len2-1)



# s = Solution()

# s_t= time.time()

# print(s.longestCommonSubsequence3('abcde', 'acfde'))

# e = time.time()

# print(e-s_t)


s = input()

len1 = len(s)
start = 0
end = 0

res = set()

for i in range(len1-1):
    if i == 0:
        end = i+1
        res.add(s[start:end])
        continue
    if s[i] == s[i-1]:
        end = i+1
        res.add(s[start:end])
    else:
        start = i
        end = i
        res.add(s[i])
print(len(res))


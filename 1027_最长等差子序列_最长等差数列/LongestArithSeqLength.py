from typing import List


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        """
        动态规划：
        1、最优子结构：每个子串可以通过遍历得到，每种等差值对应的最大序列长度
        2、转移方程：以每个短地子串中的等差值对应的最大长度 + 1
        """
        length = len(A)
        # 边界条件
        if length < 3:
            return length

        dp = [{} for i in range(length)]
        res = 0
        for i in range(1, length):
            for j in range(i):
                dis = A[i] - A[j]
                # 在前面的dp[j]中 用get()寻找dp中已有的数据。
                # 如果没有，说明是基本状态，用1初始化，+1为2
                x = dp[j].get(dis, 1)+1
                dp[i][dis] = x
            res = max(res, max(dp[i].values()))

        return res


if __name__ == "__main__":
    S = Solution()
    # S.longestArithSeqLength([3,6,9,12])
    res = S.longestArithSeqLength([1, 4, 2, 5, 3])
    print(res)

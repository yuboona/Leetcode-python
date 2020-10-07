from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        length = len(T)
        dp = [0]*length

        for i in range(length-1, -1, -1):
            if i == length-1:
                dp[i] = 0
                continue
            else:
                if T[i] < T[i+1]:
                    dp[i] = 1
                else:
                    index = i+1
                    while True:
                        if T[i] < T[index+dp[index]]:
                            dp[i] = index+dp[index]-i
                            break
                        else:
                            index = index+dp[index]
                            # 只要确保不会一直找下去就可以了——即发现再也不增长了，就直接停止
                            if dp[index] == 0:
                                dp[i] = 0
                                break
        return dp


s = Solution()
print(s.dailyTemperatures([55,38,53,81,61,93,97,32,43,78]))

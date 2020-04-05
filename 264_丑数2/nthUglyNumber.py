class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """动态规划
        使用三指针，相当于各自管理2或3或5的乘法，指针指在[1]上，这样可以按照从小到大的顺序得到后面的每个数
        （因为2、3、5乘相同的数得到的是所有最小值可能出现的地方——状态转移方程）
        
        Parameters
        ----------
        n : int
            [description]
        
        Returns
        -------
        int
            [description]
        """
        res = [1]
        i2 = 0
        i3 = 0
        i5 = 0
        for i in range(1690):
            ugly = min(res[i2]*2, res[i3]*3, res[i5]*5)
            res.append(ugly)
            if res[i2]*2 == ugly:
                i2 += 1
            if res[i3]*3 == ugly:
                i3 += 1
            if res[i5]*5 == ugly:
                i5 += 1

            if i == n:
                return res[i]


s = Solution()
s.nthUglyNumber(10)




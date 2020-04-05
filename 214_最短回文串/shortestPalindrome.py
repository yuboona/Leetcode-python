class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        1.镜像法
        """
        length = len(s)
        s_r = ''
        for i in range(length):
            s_r = s[i]+s_r
        index = 0
        for i in range(length+1):
            # 注意镜像翻转后，回文串的子串并不一定是相等的
            if(s[0:i] == s_r[-(1+i):-1]):
                index = i

        # 注意使用index作为截取  
        res = s_r[:-(1+index)] + s
        return res
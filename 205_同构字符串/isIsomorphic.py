class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        分析：这个问题
            1、直接同时遍历两个串，并判断串内前后字符串是否相同，*不能解决问题*
            2、必须要记录两个字符串之间，相互的字符间的映射。当同时遍历时，有一个不在另一个在，就是False。其他不是。
        空间复杂度：额外的两个dict，O(1)
        时间复杂度：遍历N个数据即可，O(N)
        """
        # 边界条件
        if len(s) != len(t):
            return False
        elif len(s) == 1:
            return True
        # 用两个dict记录已出现的替换，一个记录t，一个记录s，防止漏
        dic_t = {}
        dic_s = {}
        for i in range(len(s)):
            if i == 0:
                dic_t[t[i]] = s[i]
                dic_s[s[i]] = t[i]
            else:
                if t[i] in dic_t and s[i] in dic_s:
                    if dic_t[t[i]] == s[i]:
                        # 还要判断以下当前的——对应——是否是正确的对应
                        pass
                    else:
                        return False
                elif t[i] not in dic_t and s[i] not in dic_s:
                    # 两个dict都不在时
                    dic_t[t[i]] = s[i]
                    dic_s[s[i]] = t[i]
                else:
                    # 有一个不在
                    return False
                    
        return True




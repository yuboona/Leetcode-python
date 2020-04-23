class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 开一个数组，统计count
        # 时间O(2N)
        # 空间O(256) ~ O(1)
        count = [0]*256
        if len(s) != len(t):
            return False
        elif len(s) == len(t) and len(s) == 1 and s[0] == t[0]:
            return True
        else:
            len1 = len(s)
            for i in range(len1):
                count[ord(s[i])] += 1
            for i in range(len1):
                if count[ord(t[i])] == 0:
                    return False
                else:
                    count[ord(t[i])] -= 1
            return True


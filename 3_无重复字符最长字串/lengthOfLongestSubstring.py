class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []
        length = len(s)
        i = 0
        temp = []
        if length == 0:
            # 边界条件
            return 0
        if length == 1:
            return 1

        for i in range(length):
            if i == 0:
                temp.append(s[i])
                continue
            if s[i] in temp:
                res.append(''.join(temp))
                temp = [s[i]]
            elif i == length-1:
                temp.append(s[i])
                res.append(''.join(temp))
            else:
                temp.append(s[i])

        max_ = 0
        max_s = ''
        for i in res:
            if len(i) > max_:
                max_ = len(i)
                max_s = i
        return max_

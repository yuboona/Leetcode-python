class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        窗口+hashmap
        hashmap要不断删除窗口外的元素
        """
        length = len(s)

        # 边界条件
        if length == 0:
            return 0
        if length == 1:
            return 1
        if length == 2:
            if s[1] != s[0]:
                return 2
            else:
                return 1

        res = []
        i = 0
        # 用字典来装窗口的值，对应<字母:位置>
        window = {}
        for j, char in enumerate(s):
            if j == 0:
                window[char] = 0
                continue
            if char in window:
                # 最大无重复的串，放入res中
                res.append(s[i:j])
                temp_i = i
                i = window[char]+1
                for item in range(temp_i, window[char]+1):
                    window.pop(s[item])
                window[char] = j
                # 更新窗口的指针i
                if j == length-1:
                    res.append(char)
            else:
                if j == length-1:
                    res.append(s[i:])
                window[char] = j

        max_ = 0
        max_s = ''
        for i in res:
            if len(i) > max_:
                max_ = len(i)
                max_s = i
        return max_


s = Solution()
s.lengthOfLongestSubstring("abcabcbb")

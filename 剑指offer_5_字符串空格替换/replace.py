# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        out = ''
        for i in range(len(s)):
            if s[i] == ' ' or s[i] == ' ':
                out += '%20'
                continue
            out += s[i]
        return out
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = len(array)
        cloumn = len(array[0])
        if array is None or row == 0 or cloumn == 0:
            return False
        i = 0
        j = cloumn-1

        # *******************注意 i,j 是&关系，一旦有一个不满足，就不应该进行下去
        while i < row and j >= 0:
            if array[i][j] == target:
                return True
            if array[i][j] > target:
                j -= 1
                continue
            if array[i][j] < target:
                i += 1
                continue

        return False
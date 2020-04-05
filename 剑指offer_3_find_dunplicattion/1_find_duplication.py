# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    if len(numbers) < 2:
        return False
    def duplicate(self, numbers, duplication):
        # write code here
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                self.swap(numbers, i, numbers[i])
        return False
    def swap(numbers, i, num_i):
        temp = numbers[i]
        numbers[i] = numbers[num_i]
        numbers[num_i] = temp

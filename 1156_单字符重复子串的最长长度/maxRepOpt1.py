class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # FIXME 有错误，样例不通过
        # 边界条件
        length = len(text)
        if length == 1:
            return 1
        if length == 2:
            return 1

        start = 0
        end = 0
        res = []
        swap = 0

        temp = list(text)
        # for i in range(1, length): for不能完成任务
        i = 1
        while i < length:
            if temp[i] != temp[i-1] and swap == 0:
                # 不相等，没进行过swap
                for j in range(start):
                    if temp[j] == temp[i-1]:
                        # 1.找到一个j和i互换
                        _ = temp[j]
                        temp[j] = temp[i]
                        temp[i] = _
                        # swap记录了被替换的位置
                        swap = i
                        if i == length-1:
                            end = length
                            res.append(''.join(temp[start:end]))
                        # 记得找到了就退出循环，因为只能换一次
                        i += 1          # 找到了要i++
                        break
                if swap != 1:
                    # 2.在前面没有找到，到后面找
                    for j in range(length-1, i, -1):
                        if temp[j] == temp[i-1]:
                            # 找到一个j和i互换
                            _ = temp[j]
                            temp[j] = temp[i]
                            temp[i] = _
                            swap = i
                            if i == length-1:
                                end = length
                                res.append(''.join(temp[start:end]))
                            # 记得找到了就退出循环，因为只能换一次
                            i += 1      # 找到了要i++
                            break
                if swap == 0:
                    # 3.最后仍找不到可替换的，当前的窗口结束
                    end = i
                    res.append(''.join(temp[start:end]))
                    # NOTE 窗口移动
                    start = i
                    swap = 0
                    temp = list(text)
                    i += 1
            elif temp[i] != temp[i-1] and swap != 0:
                # (2) 不相等，且进行过swap
                end = i
                res.append(''.join(temp[start:end]))
                # NOTE 窗口移动

                # 将指针重新置为swap处
                start = swap
                i = swap+1
                swap = 0
                temp = list(text)
            elif i == length-1:
                # （3）相等，考虑*结尾*边界的处理
                end = length
                res.append(''.join(temp[start:end]))
                i += 1
            else:
                # （4）相等，则不用做任何事
                i += 1
        res.sort(key=lambda x: len(x))

        return len(res[-1])


s = Solution()
print(s.maxRepOpt1("aaabaaa"))
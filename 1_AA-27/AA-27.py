num = 704

# 建立对应字母的字典
dict_ = {i: chr(64+i) for i in range(1, 27)}
# 存储结果
res = []

while True:
    # 当num小于27时，表示最高位已不可进位
    if num == 0:
        break
    elif num < 27:
        res.append(num)
        break

    # temp记录从低位进位到当前位的值
    temp = num
    # 下面计算进到下一位的进位值
    if num % 26 == 0:
        num = num // 26 - 1
    else:
        num = num // 26

    # 存储进位后剩下的值，也就是这一位的值
    res.append(temp - num*26)

# 将列表逆序
res.reverse()
# 查找对应的字母
res = [dict_[i] for i in res]

print(''.join(res))

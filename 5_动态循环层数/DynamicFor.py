from functools import reduce

def RawLoopEasy():
    res = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                res += i*j*k

    print(res)


def DynamicLoopEasy():
    res = 0
    for_range = [10, 10, 10]
    ijk = []

    for code in range(reduce(lambda x, y: x*y, for_range)):
        state_decode(code, for_range)

    print(res)


def state_decode(code: int, for_range: list):
    decode = []
    tmp_code = code
    for i in range(1, len(for_range)+1):
        decode.append(tmp_code // reduce(lambda x, y: x*y, for_range[i:]))
        tmp_code = tmp_code % reduce(lambda x, y: x*y, for_range[i:])
    print(decode)


def RawLoop():
    res = 0
    for i in range(10):
        for j in range(10):
            x1 = pow(i, j)
            for k in range(10):
                for m in range(10):
                    x2 = pow(k, m)
                    res += x1+x2
    print(res)


DynamicLoopEasy()
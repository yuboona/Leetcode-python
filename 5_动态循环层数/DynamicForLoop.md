# 动态层数的for循环的实现（python实现）

## 问题描述

- 我们有时会需要实现动态层数的For循环，如下为一个简单的for循环，非常容易实现动态层数设定

```python
def RawLoopEasy():
    res = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                res += i*j*k
    print(res)
```

通过将上述for循环铺平，我们可以得到一个大循环，如下

```
def RawLoopEasy():
    res = 0
    for_range = [10, 10, 10]

    ijk = []

    for i in range(multi()):
        
    print(res)
```

```python
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


RawLoop()
```

简单的for循环
如上述代码，循环的层数还可以继续上升
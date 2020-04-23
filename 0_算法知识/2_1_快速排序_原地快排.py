import sys

sys.setrecursionlimit(9000000)      # 这里设置大一些


def quick(nums, p, r):
    if p < r:       # 递归终止条件
        q = partition(nums, p, r)
        # 用中间元素为界
        quick(nums, p, q-1)
        quick(nums, q+1, r)
        return


def partition(nums, p, r):
    mid = nums[r]       # 末尾
    i = p-1     # 从-1起始
    for j in range(p, r):
        # to r-1， 不使用最后一个元素
        if nums[j] < mid:
            i += 1
            if i != j:
                # do swap, else pass(no need swapping)
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    if i+1 != r:
        # do swap, else pass(no need swapping)
        temp = nums[i+1]
        nums[i+1] = nums[r]
        nums[r] = temp
        # i+1是最后的中间mid位置
    return i+1


def qsort(nums):
    quick(nums, 0, len(nums)-1)
    return nums


print(qsort([0, 3, 5, 7, 4, 56, 34, 36, 23, 17, 37, 43, 41, 33]))
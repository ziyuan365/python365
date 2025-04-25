# 基数排序
# 伪代码：
"""
RADIX-SORT(A, d)
for i = 1 to d
    使用稳定排序算法对数组A的第i位进行排序
"""
# 基数排序的时间复杂度为O(d * (n + k))，其中d是数字的位数，n是待排序数组的长度，k是每个位的范围（通常为10）。
# 基数排序是一种非比较排序算法，适用于整数排序，尤其是位数较少的情况。

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # 统计每个位的出现次数
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # 累加计数
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 根据计数将元素放入正确位置
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # 将排序结果复制回原数组
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

list_A = [170, 45, 75, 90, 802, 24, 2, 66]  # 待排序数组
radix_sort(list_A)
print(list_A)  # 输出排序后的数组
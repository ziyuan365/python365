# 计数排序 
# 伪代码：
"""
COUNTING-SORT(A, B, k)
let C[0..k] be a new array
for i = 0 to k 
    C[i] = 0
for j = 0 to n 
    C[A[j]] = C[A[j]] + 1
for i = 1 to k 
    C[i] = C[i] + C[i - 1]
for j = A.length down to 1
    B[C[A[j]]] = A[j]
    C[A[j]] = C[A[j]] - 1
"""
# 计数排序的时间复杂度为O(n + k)，其中n是待排序数组的长度，k是数组中元素的范围（最大值 - 最小值 + 1）。
# 计数排序的空间复杂度为O(k)，即需要额外的O(k)空间来存储计数数组C。
# 计数排序是一种非比较排序算法，适用于范围较小的整数排序。它的基本思想是统计每个元素出现的次数，然后根据这些计数来确定每个元素在排序后的位置。

list_A = [4, 2, 2, 8, 3, 3, 1] # 待排序数组
list_C = [0] * (max(list_A) + 1) # 临时存储空间
list_B = [0] * len(list_A) # 排序后的数组

for j in range(0, len(list_A)):
    list_C[list_A[j]] += 1

for i in range(1, len(list_C)):
    list_C[i] += list_C[i - 1]

for j in range(len(list_A) - 1, -1, -1):
    list_B[list_C[list_A[j]] - 1] = list_A[j]
    list_C[list_A[j]] -= 1      
    
print(list_B) # 输出排序后的数组
# 递归分治——最大子数组
import random

def FIND_MAX_CROSSING_SUBARRAY(A,low,mid,high):
    left_sum = -float('inf')
    sum = 0
    max_left = mid

    for i in range(mid,low - 1,-1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i        #确定跨越子数组的左边界，与右边界配合计算跨越子数组的最大和
    
    right_sum = -float('inf')
    sum = 0
    max_right = mid + 1

    for j in range(mid + 1,high + 1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j        #确定跨越子数组的右边界，与左边界配合计算跨越子数组的最大和

    return (max_left,max_right,left_sum + right_sum)        #返回左边界，右边界和跨越和最大子数组

def FIND_MAXIMUM_SUBARRAY(A,low,high):
    if high == low:
        return (low,high,A[low])
    else:

        mid = (low + high) // 2



        #递归求解左半部分最大子数组
        #定义三个变量并接受函数的返回值
        left_low,left_high,left_sum =  FIND_MAXIMUM_SUBARRAY(A,low,mid)         #低一层的左解    #递归调用时没有建立变量关系，递归回溯时才传入的参数

        #递归求解右半部分最大子数组
        right_low,right_high,right_sum = FIND_MAXIMUM_SUBARRAY(A,mid+1,high)        #低一层的右解



        #求解跨越中点的最大子数组               #不参与递归
        cross_low,cross_high,cross_sum = FIND_MAX_CROSSING_SUBARRAY(A,low,mid,high)         #本层的跨越解

        #比较三种情况，返回最大的子数组
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)
A = []
for i in range(9):
    number = random.randint(-10,10)
    A.append(number)
print(A)
low, high, max_sum = FIND_MAXIMUM_SUBARRAY(A, 0, len(A) - 1)
print("最大子数组:", A[low:high + 1], "和:", max_sum)
# QuickSort Algorithm Implementation in Python
# QuickSort is a divide-and-conquer algorithm that sorts an array by partitioning it into two sub-arrays,
# Pseudocode from "Introduction to Algorithms" (QuickSort):
# QUICKSORT(A, p, r)
# 1. if p < r
# 2.    q = PARTITION(A, p, r)
# 3.    QUICKSORT(A, p, q - 1)
# 4.    QUICKSORT(A, q + 1, r)
#
# PARTITION(A, p, r)
# 1. x = A[r]
# 2. i = p - 1
# 3. for j = p to r - 1
# 4.    if A[j] <= x
# 5.        i = i + 1
# 6.        exchange A[i] with A[j]
# 7. exchange A[i + 1] with A[r]
# 8. return i + 1

def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)

# Example usage:
if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5,1,3,44,22,56,74,245,4,252,6,26,453,653,642,2524,]
    print("Original array:", array)
    quicksort(array, 0, len(array) - 1)
    print("Sorted array:", array)
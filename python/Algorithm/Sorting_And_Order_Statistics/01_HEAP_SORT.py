#HEAP_SORT
#HEAP_SORT是基于堆数据结构的排序算法，具有O(n log n)的时间复杂度。
#HEAP_SORT的基本思想是将待排序的数组构建成一个最大堆，然后将堆顶元素与最后一个元素交换，并重新调整堆，直到所有元素都被排序。
#HEAP_SORT是一种不稳定的排序算法，适用于大规模数据的排序。HEAP_SORT的优点是时间复杂度较低，适用于大规模数据的排序；缺点是空间复杂度较高，需要额外的存储空间。
#HEAP_SORT在算法导论中的伪代码如下：
#HEAP_SORT(A):
# 1. BUILD-MAX-HEAP(A)  
# 2. for i = length(A) downto 2
# 3.    exchange A[1] with A[i]
# 4.    MAX-HEAPIFY(A, 1, i - 1)
# 5. return A
#HEAP_SORT的实现步骤如下：
def max_heapify(arr, n, i):
    largest = i
    left = 2 * i
    right = 2 * i + 1

    if left <= n and arr[left - 1] > arr[largest - 1]:
        largest = left

    if right <= n and arr[right - 1] > arr[largest - 1]:
        largest = right

    if largest != i:
        arr[i - 1], arr[largest - 1] = arr[largest - 1], arr[i - 1]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2, 0, -1):
        max_heapify(arr, n, i)

def heap_sort(arr):
    build_max_heap(arr)
    n = len(arr)
    for i in range(n, 0, -1):
        arr[0], arr[i - 1] = arr[i - 1], arr[0]
        max_heapify(arr, i - 1, 1)

# 使用示例
data = [12, 11, 13, 5, 6, 77, 5, 4, 33, 44, 66, 22, 22, 11, 33, 44, 55, 66, 77, 88, 99]
heap_sort(data)
print("排序后的数组:", data)
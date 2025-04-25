from collections import deque

def josephus(n, k):#k为要淘汰的人的编号  n为总人数
    queue = deque(range(1, n + 1))  # 创建一个双端队列并将队列初始化为[0，1，2，3，4，5，6，7]
    while len(queue) > 1:
        for _ in range(k - 1):  # 将前 k-1 个人移到队列尾部（一个一个移动前k-1个人）
            queue.append(queue.popleft())
        queue.popleft()  # 淘汰第 k 个人
    return queue[0]  # 返回幸存者

# 示例
n = 7
k = 3
print("幸存者的编号是:", josephus(n, k))
'''
数学解法
def josephus_math(n, k):
    result = 0
    for i in range(1, n + 1):
        result = (result + k) % i
    return result + 1
'''
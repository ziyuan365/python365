# 用递归函数计算1加到100
# 定义递归函数
def calculate_sum(n):
    if n == 1:
        return 1
    else:
        return n + calculate_sum(n - 1)

# 计算 1 到 100 的和
total = calculate_sum(100)

# 输出结果
print("1 到 100 之间所有整数的和是:", total)
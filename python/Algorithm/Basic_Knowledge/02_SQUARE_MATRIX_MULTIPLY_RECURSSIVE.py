# 递归分治——矩阵乘法
import time


start_time = time.time()
def SQUARE_MATRIX_MULTIPLY_RECURSSIVE(A, B):
    n = len(A)
    m = len(A[0]) if n > 0 else 0
    q = len(B)
    p = len(B[0]) if q > 0 else 0

    if m != q:
        raise ValueError("A的列数必须等于B的行数")

    C = [[0 for _ in range(p)] for _ in range(n)]

    # 递归终止条件
    if n <= 2 or m <= 2 or p <= 2:
        for i in range(n):
            for j in range(p):
                for k in range(m):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    # 分块（同时分割行和列）
    mid_row = n // 2  # 行分割点
    mid_col = m // 2  # 列分割点
    mid_p = p // 2    # B的列分割点

    # 分割A矩阵
    A11 = [row[:mid_col] for row in A[:mid_row]]
    A12 = [row[mid_col:] for row in A[:mid_row]]
    A21 = [row[:mid_col] for row in A[mid_row:]]
    A22 = [row[mid_col:] for row in A[mid_row:]]

    # 分割B
    B11 = [row[:mid_p] for row in B[:mid_col]]
    B12 = [row[mid_p:] for row in B[:mid_col]]
    B21 = [row[:mid_p] for row in B[mid_col:]]
    B22 = [row[mid_p:] for row in B[mid_col:]]

    # 递归计算子块
    C11 = ADD_MATRIX(SQUARE_MATRIX_MULTIPLY_RECURSSIVE(A11, B11), SQUARE_MATRIX_MULTIPLY_RECURSSIVE(A12, B21))
    C12 = ADD_MATRIX(SQUARE_MATRIX_MULTIPLY_RECURSSIVE(A11, B12), SQUARE_MATRIX_MULTIPLY_RECURSSIVE(A12, B22))
    C21 = ADD_MATRIX(SQUARE_MATRIX_MULTIPLY_RECURSSIVE(A21, B11), SQUARE_MATRIX_MULTIPLY_RECURSSIVE(A22, B21))
    C22 = ADD_MATRIX(SQUARE_MATRIX_MULTIPLY_RECURSSIVE(A21, B12), SQUARE_MATRIX_MULTIPLY_RECURSSIVE(A22, B22))

    # 合并子块
    for i in range(len(C11)):
        for j in range(len(C11[0])):
            C[i][j] = C11[i][j]
            C[i][j + len(C11[0])] = C12[i][j]       #c[1][j+len(c11(0))]的作用是让c12的列跳过c11已填充的列，但是行不变
    for i in range(len(C21)):
        for j in range(len(C21[0])):
            C[i + len(C11)][j] = C21[i][j]
            C[i + len(C11)][j + len(C21[0])] = C22[i][j]
    return C

def ADD_MATRIX(X, Y):
    """矩阵加法辅助函数"""
    return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
B = [[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]]
result = SQUARE_MATRIX_MULTIPLY_RECURSSIVE(A, B)  # 4×4 分块乘法
print(result)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"代码运行时间: {elapsed_time:.6f} 秒")
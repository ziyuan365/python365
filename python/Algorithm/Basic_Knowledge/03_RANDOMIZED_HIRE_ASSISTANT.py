# 随机算法——雇佣问题
import random

def randomized_hire_assistant(candidates):
    random.shuffle(candidates)  # 关键步骤：随机排列
    best = float('-inf')
    hire_count = 0
    hired_candidates = []
    
    for candidate in candidates:
        if candidate > best:
            best = candidate
            hire_count += 1
            hired_candidates.append(candidate)
    
    print(f"Hired {hire_count} candidates: {hired_candidates}")
    return hire_count

# 测试
candidates = [1, 2, 3, 4, 5]
total_hire = 0
trials = 1000

for _ in range(trials):
    total_hire += randomized_hire_assistant(candidates.copy())

print(f"平均雇佣次数：{total_hire / trials}")
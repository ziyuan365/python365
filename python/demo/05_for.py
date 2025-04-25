print("###################")
# 创建一个列表并遍历输出列表中的元素
print("for_demo_01:")
names=['jack','tom','mark']
for name in names:
    print(name)

print("###################")




print("for_demo_02:")
# 定义一个变量作为平方和的结果
sum=0
for i in (1,2,3,4,5,6,7,8,9):#迭代数据
    sum+=i**2                #等于sum=sum+i**2
print(sum)

print("###################")




print("for_demo_03:")
# 定义一个变量用于存储和
result=0
for j in range(1001):#使用range()函数创建一个0~1000的整数序列   详情解释看：02_expression_demo1
    result+=j        #等于result=result+j
print(result)

print("###################")




print("for_demo_04:")
#用for循环输出九九乘法表
for row in range(1,10):
    for col in range(1,row+1):
        print('{0}*{1}={2}'.format(row,col,row*col),end=" ")
    print("")        #换行放在外循环
print("###################")
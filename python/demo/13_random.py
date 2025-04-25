print("###################")
print("random_demo_01:")
import random 
# while True:
num=random.randint(1,10)
print(num)



print("###################")
print("random_demo_02:")
random_list=[]
for i in range(10):         #产生十次随机数
    random_number=random.randint(1,100)         #随机数分布于（1，100）
    random_list.append(random_number)           #将随机产生的数赋给列表
print("原数组为：",random_list)
#冒泡排序
for i in range(0,len(random_list)-1):
    for j in range(0,len(random_list)-i-1):
        if random_list[j]>random_list[j+1]:
            random_list[j],random_list[j+1]=random_list[j+1],random_list[j]
print("排序后的数组为：",random_list)



print("###################")
print("random_demo_03:")
random_list=[]
for i in range(10):
    random_number=random.uniform(1.0,10.0)
    random_list.append(round(random_number,2))
print("原数组为：",random_list)
for i in range(0,len(random_list)-1):
    for j in range (0,len(random_list)-i):      #line34&line35 避免j超出列表长度 与line19&line20对比
        if random_list[j-1]<random_list[j]:
            random_list[j-1],random_list[j]=random_list[j],random_list[j-1]
print("排序后的数组为：",random_list)         

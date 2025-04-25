my_list=list(range(1,1001))     #定义一个数组从1到1000
times=0     #初始化
for num in my_list:
    if num%3==0 and num%5==0:   #条件
        print(num)
        times+=1        #累加
    else:
        continue
    if times==6:        #条件
        break

#pass占位:仅起到展位作用，本处不执行循环
while True:
    pass
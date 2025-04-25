print("###################")
print("work_02_01(page:073 T6):")
sum=0
while True:
    number=int(input("请输入数据："))
    if number<0:
        break
    else:
        sum=sum+number
print("和为：",sum)



print("###################")
print("work_02_01(page:073 T9):")
sums=1
while True:
    num=int(input("请输入一个非负整数："))
    if num<0:
        (print("输入数字无效，请按要求输入"))
        continue
    else:
        for i in range(1,num+1):
            sums=sums*i
        print("你输入数字的阶乘为：",sums)
    break

            
    



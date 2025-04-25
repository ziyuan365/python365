print("###################")
print("while_demo_01:")
sum=0                   #定义一个变量用于存放100以内奇数和的值
num=99
while num>0:
    sum=sum+num
    num-=2              #num=num-2
print("一百以内奇数和为",sum)



print("###################")
print("while_demo_02:")
#用while循环输出九九乘法表
row=1
while row<=9:
    col=1
    while col<=row:
        print('{0}*{1}={2}'.format(row,col,row*col),end=" ")
        col=col+1
        # print("")      内层循环不能嵌套换行！！！

    print("")
    row=row+1
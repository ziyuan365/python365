#素数
import random

user_input=int(input("请输入一个数字："))
def func(user_input):
    my_list=[]
    for i in range(2,int(user_input)):
        my_list.append(i)
    print("生成的数组为：",my_list)
    #添加一个变量，由它的变化来实现循环
    is_prime=True

    for j in my_list:
        if user_input%j!=0:
            continue
        else:
            print(str(user_input)+"不是素数")
            #如果不是素数则is_prime发生变化，覆盖掉之前的赋值True改为False
            is_prime=False

            break
    #循环结束后 is_prime 仍为 True则(is_prime可以是任何类型，布尔型，int，str等等)：
    if is_prime==True:
        print(str(user_input)+"是素数")        
func(user_input)





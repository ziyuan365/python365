print("###################")
print("return_demo_01:")
def showplus(x): 
    return x 
    # print(x)
num=showplus(6)
print(num)
print(type(num))



print("###################")
print("return_demo_02:")
def showplus(x):
    print(x)
    return x+1
    print(x+2)          #函数以return结尾，不再进行计算
print(showplus(6))



print("###################")
print("return_demo_03:")
def outer():
    def inner():
        print('inner')
    print('outer')
    inner()         #嵌套函数不能被直接调用在outer函数内部才能被调用
outer()
# inner()
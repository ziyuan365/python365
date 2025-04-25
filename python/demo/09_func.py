print("###################")
print("func_demo_01:")
def my_hanshu(a):
    d=0
    for c in a:
        d=d+1
    return d
b=my_hanshu("666666666")
print(b)



print("###################")
print("wfunc_demo_02:")
# 对比返回值（return）
def str_max(str1,str2):
    str=str1 if str1>str2 else str2
    return str
r=str_max(5,1)
print(r)
print("#####")
def str_max(str1,str2):
    return str1 if str1>str2 else str2
r=str_max(1,2)
print(r)




print("###################")
print("wfunc_demo_03:")
def plus(a,b):
    c=a+b
    return c
d=plus(3,4)
print(d)



print("###################")
print("wfunc_demo_04:")
def function(a,l=[]):
    l.append(a)         #向列表添加元素
    return l
print(function(1))
print(function(1))
print(function(3))
print(function(4))


print("###################")
print("wfunc_demo_05:")
num1=int(input("请输入第一个数："))
num2=int(input("请输入第二个数："))
def compera_number(a,b):            #定义一个函数并传入参数
    if a>b:
        print("{0}>{1}".format(a,b))
    elif a==b:
        print("{0}={1}".format(a,b))
    else:
        print("{0}<{1}".format(a,b))
        # return 无返回值，默认返回
compera_number(num1,num2)           #调用函数



print("###################")
print("wfunc_demo_06:")
n=int(input("请输入一个数字:"))
def power_add(n):
    sum=0                           #定义总和
    for i in range(1,n+1):          #for循环遍历
        sum=sum+pow(i,2)            #pow为（i，2）表示i的平方，pow（a，b）表似a的b次方
    print("前n项的平方和为:",sum)
power_add(n)                        #调用函数



print("###################")
print("wfunc_demo_07:")
string=input("请输入一个字符串：")
def split_string(string):       #定义函数
    str_list=[]                 #创建一个空列表用来储存字符
    for str in string:          #遍历用户输入的字符串
        str_list.append(str)    #将遍历的字符串储存至str_list空列表中
    #实现排序
    for i in range(0,len(str_list)-1):  #每次循环都会把最小的数字放在最后，所以只需要n-1次
        for j in range(0,len(str_list)-i-1):#经过i轮循环已经有i个字符被放在正确的位置上，所以减去i减少排序
            if str_list[j]<str_list[j+1]:
                str_list[j],str_list[j+1]=str_list[j+1],str_list[j]
    for str in str_list:
        if str !=str_list[-1]:#str_list[-1]是列表最后一个元素
            if str==" ":
                str="空格"
            print(str,end='>')#end='>'表示不换行
        else:
            if str==" ":
                str="空格"
            print(str)
split_string(string)




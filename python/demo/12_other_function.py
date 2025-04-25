print("###################")
print("map高阶函数:")
def f(x):
    return x*x
result=map(f,[1,2,3,4,5,6,7])   #接收一个f函数和一个列表list，将函数f作用到列表list的每一个元素上得到一个新的列表
print(list(result))



print("###################")
print("reduce高阶函数:")
from functools import reduce     #导入reduce函数
def f(x,y):
    return x*y
print(reduce(f,[1,2,3,4]))       #1*2*3*4=24
def f1(a,b):
    return a+b
print(reduce(f1,[1,2,3,4],10))   #1+2+3+4+10这里第三个参数是作为初始值的



print("###################")
print("sorted高阶函数:")
students=[('John','A',15),('Jane','B',12),('Dave','B',10)]
students1=sorted(students,key=lambda s:s[2])        #本实验要求按照年龄排序，即按照列表第三个参数排序，所以取s[2]
print(students1)
print("#######")
students2=sorted(students,key=lambda s:s[2],reverse=True)       #降序排列
print(students2)

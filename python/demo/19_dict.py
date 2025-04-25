import random
print("###################")
print("dict_demo_01:")
my_dict={}
for number in range(65,91):
    char=chr(number)        #在ASCLL码表中获取对应数字的英文字母并赋给char
    my_dict[char]=number    #将char作为键，将number作为值
print(my_dict)



print("###################")
print("dict_demo_02:")
my_dict={}
for i in range(26):
    char=chr(random.randint(65,91))
    #向字典中添加元素
    my_dict[char]=ord(char)
for i in range(3):
    pass
    # char=input("请输入一个字符：")
    # if char in my_dict:
    #     print("存在"+char+"这个键，它的值为："+str(my_dict[char]))
    # else:
    #     print("不存在"+char+"这个键")
print("字典为：",my_dict)



print("###################")
print("dict_demo_03:")
my_dict=dict()
for number in range(97,123):
    char=chr(number)
    my_dict[char]=number
swap_dict=dict()
for key in my_dict:
    #实现键和值的交换
    value=my_dict[key]
    swap_dict[value]=key
    #
print("原字典为：",my_dict)
print("新字典为：",swap_dict)
new_dict={value:key for key,value in my_dict.items()}
print("新字典为：",new_dict)



print("###################")
print("dict_get()_demo_04:")
student_dict=dict()
# name=input("请输入你的姓名：")
# student_dict['name']=name
# age=int(input("请输入你的年龄："))
# student_dict['age']=age
# id=input("请输入你的学号：")
# student_dict['id']=id
# chinese_score=int(input("请输入你的语文成绩："))
# student_dict['chinese']=chinese_score
# math_score=int(input("请输入你的数学成绩："))
# student_dict['math']=math_score
#访问信息
print("学生信息字典为：",student_dict)
print("学生数学成绩为：",student_dict.get('math',99))



print("###################")
print("dict_keys()_demo_05:")
my_dict=dict()
for i in range(8):
    number=random.randint(65,90)
    char=chr(number)
    my_dict[char]=number
print(my_dict)
for key in my_dict.keys():
    print(key,my_dict.get(key))
#itmes()->一元组的形式返回字典的键和值
# for key,number in my_dict.items():
#     print(key,number)



print("###################")
print("dict_pop()_demo_06:")
my_dict=dict()
for number in range(65,91):
    char=chr(number)
    my_dict[char]=number
print("原字典为：",my_dict)
for key in my_dict.copy():          #.copy()->遍历副本，防止RuntimeError
    if key<'K':
        my_dict.pop(key)
print("删除后的字典：",my_dict)



print("###################")
print("dict_popitem()_demo_07:")
my_dict=dict()
for items in range(11):
    number=random.randint(97,122)
    char=chr(number)
    my_dict[char]=number
print("原字典为：",my_dict)
pop_list=[]
for i in range(5):
    k,v=my_dict.popitem()       #其他情况下不用读键值对进行存储，可以直接使用dict.popitem()对键值对进行删除

    #删除的键值对用元组储存
    pop_tuple=(k,v)
    pop_list.append(pop_tuple)
print("删除的键值对为：",pop_list)
print("删除元素后的字典为：",my_dict)
#遍历删除的键值对
for item in pop_list:
    print(item)



print("###################")
print("dict_values()_demo_08:")
print("values()返回字典中所有的值,类似于keys()方法")



print("###################")
print("dict_demo_09:")

'''
用户在控制台输入字符串，用字典存储字符串的每个字符的个数，并输出最多的字符和最少的字符
'''

# string=input("请输入字符串：")
char_dict=dict()
# for char in string:
#     #如果char没在字典中，将这个字符作为键添加到自带你中，值为1,由于char_dict本就是空字典，所以该部分的含义是字符计数
#     if char not in char_dict:
#         char_dict[char]=1       #这里值为1，即字典的值是计数的工具
#     #如果char在字典中，则在原先的基础上加1
#     else:
#         char_dict[char]=char_dict[char]+1   #计数
print("字典为：",char_dict)
#创建列表
char_list=[]
for k,v in char_dict.items():       #char_dict.items()在for循环中的作用是，返回字典中key和value的值并分别赋给k和v
    char_list.append((k,v))         #将k，v的值添加到列表中
#使用sorted()函数对字典元素的个数进行排序
# sorted(char_list, key=lambda x: x[1]) 的作用是对 char_list 进行排序，排序的依据（key）是每个元素的 第 2 个值（x[1]）
char_list=sorted(char_list,key=lambda x:x[1])
print("列表为：",char_list)
# print("最少的元素使：{0},数目是：{1}".format(char_list[0][0],char_list[0][1]))
# print("最多的元素使：{0},数目是：{1}".format(char_list[-1][0],char_list[-1][1]))



print("###################")
print("dict_demo_10:")
'''
字母加密，要求用户输入一串小写英文字母，并创建一个加密字典，对{a:z,c:l,g:%,z:@a:z,c:l,g:%,z:@}进行加密
'''
#创建加密字典
security_dict={"a":'z','c':'l','g':'%','z':'@'}
#用户输入字符串

# string=input("请输入一串小写字母：")

#加密
security_string=''
# for char in string:
#     if char in security_dict:
#         security_string=security_string+security_dict[char]
#     else:
#         security_string=security_string+char
# print("原字符串：",string)
print("加密后的字符串",security_string)
#使用列表推导式进行解密
open_dict={value:key for key,value in security_dict.items()}
open_string=''
for char in security_string:
    pass
    # if char in open_dict:
    #     open_string=open_string+open_dict[char]
    # else:
    #     open_string=open_string+char

print("解密后的字符串",open_string)



print("###################")
print("dict_demo_11:")
#输入一个字符串，输出字符串中出现的字符
#用户在控制台输入一个字符串
string=input("请输入一个字符串：")
char_dict={}
for char in string:
    if char not in char_dict:
        char_dict[char]=""      #将string的值作为一个键保存起来，值为空
    else:
        pass
print("出现的字符有：")
for char in char_dict.keys():
    print(char)

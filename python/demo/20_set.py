import random
#集合及其操作
print("###################")
print("set()_demo_01:")
#统计一个字符串中出现的所有字符（集合不算重复元素）

# string=input("请输入一个字符串：")

#创建一个空集合
my_set=set()

# my_set.update(string)

#将集合转化为列表并输出
my_list=list(my_set)
for char in my_list:
    print(char,end=" ")     #end=" "将输出结果变为一行



print("###################")
print("set()_demo_02:")
random_list=[]
times=0
for i in range(10):
    number=random.randint(1,20)
    if number not in random_list:
        random_list.append(number)
        times+=1
    if times==10:
        break
random_set=set(random_list)     #创建内元素为random_list的集合
print("集合为：",random_set)
remove_set=set()    #创建空集合
for number in random_set:
    if number%2==0:
        remove_set.add(number)      #向remove_set集合中添加要删除的元素
print("删除偶数后集合为：",random_set-remove_set)       #两个集合做减法，得出剩下的集合



print("###################")
print("set_MathMathod_demo_03:")
'''
集合具有交并差补的特点，其中特殊的为对称差集即为两集合的交集之于其并集的补集
'''
my_set1=set()
my_set2=set()
for i in range(5):
    number1=random.randint(1,10)
    number2=random.randint(1,10)
    my_set1.add(number1)
    my_set2.add(number2)
print("集合1为:",my_set1)
print("集合2为:",my_set2)
print("集合1和集合2的并集为:",my_set1.union(my_set2))
print("集合1和集合2的并集为:",my_set1|my_set2)
print("集合1和集合2的交集为:",my_set1.intersection(my_set2))
print("集合1和集合2的交集为:",my_set1.intersection(my_set2))
print("集合1和集合2的差集为:",my_set1.difference(my_set2))
print("集合1和集合2的差集为:",my_set1-my_set2)
print("集合1和集合2的对称差集为:",my_set1.symmetric_difference(my_set2))
print("集合1和集合2的对称差集为:",my_set1^my_set2)
print("集合1是集合2的子集:",my_set1.issubset(my_set2))
print("集合2是集合1的子集:",my_set2.issubset(my_set1))
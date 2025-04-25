import random
print("###################")
print("list_demo_01:")
my_list=[1,2,3,4,5]
print("原列表为：",my_list)
for i in range(len(my_list)):
    my_list[i]=my_list[len(my_list)-i-1]        #列表实现了覆盖输出不了【5，4，3，2，1】
print("修改后的列表为：",my_list)



print("###################")
print("list_demo_02:")
random_list1=[random.randint(1,20)for x in range(5)]            #生成”不同“随机数列表
random_list2=[random.randint(1,20)for y in range(5)]
print("数组1:",random_list1)
print("数组2:",random_list2)
random_list3=random_list1+random_list2
print("数组3:",random_list3)
for i in range (0,len(random_list3)-1):
    for j in range(0,len(random_list3)-i-1):
        if random_list3[j]>random_list3[j+1]:
            random_list3[j],random_list3[j+1]=random_list3[j+1],random_list3[j]
print("排序后的数组：",random_list3)



print("###################")
print("list_demo_03:")
# random.seed(10)         #添加种子，产生相同随机数
my_list=[]
for i in range(10):
    number=random.randint(1,20)
    my_list.append(number)
print("列表为：",my_list)
print("截取全部的数：",my_list[:])
print("截取第二个到第五个数：",my_list[2:6])        #列表的个数从第0个数开始
print("截取倒数的六个数：",my_list[-6:])            #从倒数第六个开始索引
print("截取从第一个元素开始步长为二的所有数：",my_list[::2])



print("###################")
print("list_demo_04_append():")
my_list=[]
for i in range(5):
    pass
    # user_input=input("请输入第"+str(i+1)+"个数据")
    # my_list.append(user_input)
    # print(my_list)




print("###################")
print("list_demo_05_index():")
my_list=[]
for i in range(5):
    pass
    # user_input=input("输入第"+str(i+1)+"个数据：")
    # my_list.append(user_input)
print(my_list)
for i in my_list:
    pass
    # print(i+"下标为："+str(my_list.index(i)))



print("###################")
print("list_demo_06_insert():")
my_list=[]
for i in range(5):
    pass
    # insert_location=random.randint(0,4)
    # user_input=input("请输入数据：")
    # print("插入到下标为"+str(insert_location)+"的位置")     #字符串的拼接转化
    # my_list.insert(insert_location,user_input)

# for v in my_list:         #遍历数组赋给v
#     print(v)
print(my_list)



print("###################")
print("list_demo_07_sort():")
my_list=[]
for i in range(1,6):
    pass
    # user_input=input("请输入第"+str(i)+"个数字")
    # my_list.append(user_input)
print("原列表为：",my_list)
my_list.sort()
print("排序后的列表为：",my_list)



print("###################")
print("list_demo_08_sort()_string:")
my_list=[]
for i in range(1,6):
    pass
    # input_str=input("请输入第"+str(i)+"个字符串")
    # my_list.append(input_str)
print("原列表为：",my_list)
my_list.sort()
print("排序后的列表为：",my_list)



print("###################")
print("list_demo_09_remove():")
my_list=[]
for i in range(1,6):
    pass
    # user_input=input("请输入第"+str(i)+("个数据"))
    # my_list.append(user_input)
print(my_list)
for i in range(2):
    pass
    # index=random.randint(0,len(my_list)-1)
    # print("删除了第"+str(index)+("个元素"))
    # my_list.remove(my_list[index])
print(my_list)



print("###################")
print("list_demo_10_reverse():")
string_list=[]
number_list=[]
for i in range(10):
    pass
    # String=chr(random.randint(65,90))
    # string_list.append(String)
for i in range(10):
    pass
    # number=random.randint(1,10)
    # number_list.append(number)
print("原字符列表：",string_list)
string_list.reverse()
print("倒序后的字符列表：",string_list)
print("原数值列表：",number_list)
number_list.reverse()
print("倒序后的数值列表：",number_list)



print("###################")
print("list_demo_11_del:")
my_list=[]
for i in range(1,6):
    pass
    # user_input=input("请输入第"+str(i)+"个数据")
    # my_list.append(user_input)
print("原列表：",my_list)
for i in range(2):
    pass
    # del my_list[random.randint(0,len(my_list)-1)]           #相较于remove，del是直接删除
    # print("删除后的列表：",my_list)



print("###################")
print("list_demo_12_min()&max()_01:")
my_list=[]
for i in range(10):
    pass
    # number=random.randint(1,100)
    # my_list.append(number)
print("排序前的列表：",my_list)
for i in range(0,len(my_list)-1):
    pass
    # for j in range(0,len(my_list)-i-1):
    #     if my_list[j]>my_list[j+1]:
    #         my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
print("排序好后的列表：",my_list)
# print("列表中的最大值：",max(my_list))
# print("列表中的最小值：",min(my_list))



print("###################")
print("list_demo_12_min()&max()_02(str):")
my_list=[]
for i in range(10):
    pass
    # string=chr(random.randint(65,90))
    # my_list.append(string)
print("排序前的列表：",my_list)
for i in range(0,len(my_list)-1):
    pass
    # for j in range(0,len(my_list)-i-1):
    #     if my_list[j]>my_list[j+1]:
    #         my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
print("排序后的列表：",my_list)
# print("列表中的最大值：",max(my_list))
# print("列表中的最小值：",min(my_list))



print("###################")
print("list_demo_13_CopyList:")
my_list1=[1,2,3,4,5]
my_list2=[]
for item in my_list1:
    my_list2.append(item)
print(my_list2)



print("###################")
print("list_demo_14:")
my_list=[]
for i in range(10):
    number=random.randint(1,100)
    my_list.append(number)
print(my_list)
sum_my_list=0           #初始化/定义
for number in my_list:  #求和
    sum_my_list=sum_my_list+number
print("列表中元素的和为：",sum_my_list)
print("列表中元素的和为：",sum(my_list))



print("###################")
print("list_demo_15:")
my_list=[]
for i in range(10):
    number=random.randint(1,50)
    my_list.append(number)
print(my_list)
sum_my_list=0
for number in my_list:
    sum_my_list=sum_my_list+number
print("列表中元素的平均值为：",sum_my_list/len(my_list))



print("###################")
print("list_demo_16:")
# my_list=list(map(str,input("请以空格为分隔符输入十个数据：").split(" ")))
print(my_list)
number=0
string=""
for item in my_list:
    try:
        if isinstance(int(item),int):
            number=number+int(item)
    except:
        string=string+item
print("列表中所有数值的和为：",number)
print("列表中所有字符串拼接为：",string)



print("###################")
print("list_demo_17:")
my_list=[[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(3):
    for j in range(3):
        number=random.randint(1,10)
        my_list[i][j]=number
print("二维表格为：",my_list)
for i in range(3):
    for j in range(3):
        print("第{0}行第{1}列的元素是：{2}".format(i,j,my_list[i][j]))



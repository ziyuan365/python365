import random
print("###################")
print("String_demo_-01:")
# string=input("请输入一个字符串：")
# for str in string:
#     print(str,end=" ")
# for i in range(len(string)):
#     print(string[-i-1],end=" ",)



print("###################")
print("String_demo_02:")
my_string=' '
letter_list=[]
for number in range(97,123):
    char=chr(number)
    letter_list.append(char)
for char in letter_list:
    my_string=my_string+char+' '
print("拼接后的字母字符串为：",my_string)



print("###################")
print("String_demo_03:")
char_list=[]
for i in range(10):
    pass
    # char=chr(random.randint(50,100))
    # char_list.append(char)
    # my_string=' '
    # for char in char_list:
    #     my_string=my_string+char
# char=input("请输入一个字符：")
if char not in my_string:
    print(char+'不存在于字符串当中')
else:
    print(char+"存在于字符串当中")
print("字符串为",my_string)



print("###################")
print("String_demo_04:")
# my_string=input("请输入字串：")
string_list=[]
string_num_list=[]
for char in my_string:
    pass
    # if char not in string_list:
    #     string_list.append(char)
    #     string_num_list.append([char,1])
    # else:
    #     #遍历字符串，字符出现一次便加一
    #     i=0
    #     for string in string_num_list:
    #         if char!=string[0]:         #string不是字符本身而是子列表['h',1]等等
    #             i+=1
    #         else:
    #             string_num_list[i][1]+=1
string_num_list=sorted(string_num_list,key=lambda x:x[1])
print(string_num_list)
# print("出现次数最多的字符为：{0}，出现次数为：{1}".format(string_num_list[-1][0],string_num_list[-1][1]))



print("###################")
print("String_demo_05:")
# my_string=input("请输入字符串：")
new_string=''
for char in my_string:
    #判断char是否是大写，且判断该字符在my_string中是否不是第一个字符
    pass
    # if char.isupper() and my_string.index(char)!=0:
    #     new_string=new_string+' '+char
    # else:
    #     new_string=new_string+char
print("原字符串为：",my_string)
print("分割后的字符串为：",new_string)



print("###################")
print("String_demo_06:")
# 字符分析，输入一个字符，统计出大写字母，小写字母，数字字符，空白字符，yijiqita字符的数量
my_string=input("请输入需要统计的字符串：")
upper_char=0
lower_char=0
space_char=0
other_char=0
digit_char=0
for char in my_string:
    if char.isupper():
        upper_char=upper_char+1
    elif char.islower():
        lower_char=lower_char+1
    elif char.isspace():
        space_char=space_char+1
    elif char.isdigit():
        digit_char=digit_char+1
    else:
        other_char=other_char+1
print("字符串为：",my_string)
print("大写字母数为：",upper_char)
print("小写字母数为：",lower_char)
print("空格字符数为：",space_char)
print("数字字符数为：",digit_char)
print("其他字符数为：",other_char)
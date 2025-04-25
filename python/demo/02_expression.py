length=int(input("请输入数组的长度："))
my_list=[chr(x) for x in range (65,65+length)]#for A in B 的作用是将B循环一次赋值给A    (for变量in序列)
print(my_list)
for char in my_list:
    print(char)

#print(chr(65))将65转为Unicode码A
#range（）生成整数序列
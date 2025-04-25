length=int(input("请输入长方形长："))#input函数的返回值是字符串（str型），所以要用int（）进行字符转换
width=int(input("请输入长方形的宽："))
area=length*width
print("长方形的面积是：",area)#print("长方形的面积是："+area)u不可以用+连接int型只可以连接str型
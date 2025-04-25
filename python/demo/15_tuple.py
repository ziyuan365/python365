import random
my_tuple=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        number=random.randint(1,10)
        my_tuple[i][j]=number
print("元组为：",my_tuple)
print("列表为：",list(my_tuple))
for i in range(3):
    for j in range(3):
        print("元组第{0}行第{1}列的元素是:{2}".format(i,j,my_tuple[i][j]))




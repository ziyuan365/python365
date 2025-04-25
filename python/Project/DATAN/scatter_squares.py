#
import matplotlib.pyplot as plt

x_value = range(1,1001)
y_value = [x**2 for x in x_value]

plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()
ax.scatter(x_value,y_value,color=(0,0.8,0),s=10)        #普通颜色
ax.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Blues,s=10)        #蓝色映射模式

#设置图题并给坐标加上标签
ax.set_title('Square Numbers',fontsize=24)
ax.set_xlabel('Value',fontsize=14)
ax.set_ylabel('Square of Value',fontsize=14)

#设置每个坐标轴的取值范围
ax.axis([0,1100,0,1_100_000])
# ax.ticklabel_format(style='plain')        #不使用科学计数法

#设置刻度标记的样式
ax.tick_params(labelsize=14)


plt.savefig(r'D:\code\python\Project\DATAN\image\squares_plot.png',bbox_inches='tight')
plt.show()
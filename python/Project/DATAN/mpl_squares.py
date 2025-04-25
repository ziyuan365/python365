#绘制折线图
#square存储折线数据，经由ax的plot方法调用数据，绘制折线图
import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

# print(plt.style.available)
plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()     #创建一个图形（fig）和坐标轴（ax）对象
ax.plot(input_values,squares,linewidth=3)       #在坐标轴（ax）上绘制图形（fig折线图）

#设置图题并给坐标轴加上标签
ax.set_title('Square Numbers',fontsize=24)
ax.set_xlabel('Value',fontsize=14)
ax.set_ylabel('Square of Value',fontsize=14)

#设置刻度标记样式
ax.tick_params(labelsize=14)

plt.show()
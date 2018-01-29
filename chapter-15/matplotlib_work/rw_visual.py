# 漫步图
import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw=RandomWalk()
rw.fill_walk()
plt.figure(figsize=(10, 6))
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
 edgecolor='none', s=1)
#  绘制开始和结束的散点
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
 s=100)
plt.title("hey jude")
plt.xlabel("annilq",fontsize=14)
plt.ylabel("jude",fontsize=14)
# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.savefig('squares_plot3.png', bbox_inches='tight')
plt.show()
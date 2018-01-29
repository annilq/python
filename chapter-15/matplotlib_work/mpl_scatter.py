# 散点图
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none',  s=100)
plt.title("hey jude")
plt.xlabel("annilq",fontsize=14)
plt.ylabel("jude",fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.savefig('squares_plot.png', bbox_inches='tight') 
plt.show()
# 折线图
import matplotlib.pyplot as plt

input_squares=[1,2,3,4,5]
squares=[1,4,9,16,25]
plt.plot(input_squares,squares,linewidth=5)
plt.title("hey jude")
plt.xlabel("annilq",fontsize=14)
plt.ylabel("jude",fontsize=14)
plt.tick_params(axis='both', labelsize=14) 
plt.show()
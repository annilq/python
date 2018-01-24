import pygal
from die import Die

my_die=Die()
result=[]
for i in range(100):
    side=my_die.roll_die()
    result.append(side)
# print(result)


# 分析结果
frequencies = [] 
for side in range(1,my_die.sides+1):
    side_count=result.count(side)
    frequencies.append(side_count)
print(frequencies)



hist = pygal.Bar()
hist.title="每个点数出现的次数"
hist.x_labels=["1","2","3","4","5","6"]
hist.x_title="result"
hist.y_title="次数"
hist.add("D6",frequencies)
hist.render_to_file("die_visual.svg")

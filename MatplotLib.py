import matplotlib.pyplot as plt
import numpy as np
'''''
x = np.arange(0,10)
y = np.arange(11,21)
plt.scatter(x,y)
plt.xlabel("X axis")
plt.ylabel("yaxis")
plt.title("Hey")
plt.show()

y = x**3

plt.plot(x,y,'y.',linestyle='dashed',linewidth=2,markersize=12)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("2D Diagram")
plt.show()

##Barplot
x = [2,8,10]
y = [11,16,9]

x2 = [3,9,11]
y2 = [6,15,7]

plt.bar(x,y)
plt.bar(x2,y2,color='g')

plt.title("Bar Graph")
plt.ylabel("Y axis")
plt.xlabel("X axis")
plt.show()

'''

#pie chart
#Data
labels = 'Python', 'C++','Ruby', 'Java'
sizes = [215,130,245,210]
colors=["gold","yellowgreen","lightcoral","lightskyblue"]
ex = (0.4,0.2,0.1,0.8)
#plot
plt.pie(sizes,labels=labels,colors=colors,explode= ex, autopct='%1.1f%%')

plt.axis("equal")
plt.show()

import matplotlib as plt 
print(plt.__version__)

import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [3, 2, 1]
plt.plot(x, y)
plt.title("Line Chart")
plt.legend(["Line"])
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0.1, 2 * np.pi, 41)
y = np.exp(np.sin(x))
plt.title("Stem plot")
plt.stem(x, y)
plt.show()

x = [3, 1, 3, 12, 2, 4, 4]
y = [3, 2, 1, 4, 5, 6, 7]
plt.bar(x, y)
plt.title("Bar Chart")
plt.legend("bar")
plt.show()

x = [1, 2, 3, 4, 5, 6, 7, 4]
plt.hist(x, bins = [1, 2, 3, 4, 5, 6, 7])
plt.title("Histogram")
plt.legend("Bar")
plt.show()

x = [3, 1, 3, 12, 2, 4, 4]
y = [3, 2, 1, 4, 5, 6, 7]
plt.scatter(x, y)
plt.title("Scatter Chart")
plt.legend("A")
plt.show()

import numpy as np
np.random.seed(10)
data = np.random.normal(100, 20, 200)
fig = plt.figure(figsize =(10, 7))
plt.boxplot(data)
plt.show()

x = [1, 2, 3, 4, 5]
e  =(0.1, 0, 0, 0, 0)
plt.pie(x, explode = e)
plt.title("Pie chart")
plt.show()

x =[1, 2, 3, 4, 5, 6, 7]
y =[1, 2, 1, 2, 1, 2, 1]
y_error = 0.2
plt.plot(x, y)
plt.errorbar(x, y,yerr = y_error,fmt ='o')

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
z = [1, 8, 27, 64, 125]
fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot3D(z, y, x)


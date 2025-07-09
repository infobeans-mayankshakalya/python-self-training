from matplotlib import pyplot as plt
from numpy import *
from datetime import datetime, timedelta
import random

# Generate all days in June 2025
x_axis = [(datetime(2025, 6, 1) + timedelta(days=i)).strftime("%d") for i in range(30)]
# Example data: random earthquake scale for each day
y_axis = [round(random.uniform(1.0, 7.0), 1) for _ in x_axis]

print(x_axis)
print(y_axis)
plt.title('Japan Earthquakes in June')
plt.xlabel('Day')
plt.ylabel('Magnitude')
plt.grid(linestyle='-', linewidth=0.5, axis='y')
plt.plot(x_axis,y_axis)
plt.scatter(x_axis,y_axis)
# plt.bar(x_axis,y_axis)
plt.show()
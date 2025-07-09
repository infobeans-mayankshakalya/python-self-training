from matplotlib import pyplot as plt
from numpy import *
from datetime import datetime, timedelta
import random

# Generate all days in June 2025
x_axis = [(datetime(2025, 6, 1) + timedelta(days=i)).strftime("%d") for i in range(30)]
# Example data: random earthquake scale for each day
y1_axis = [round(random.uniform(1.0, 7.0), 1) for _ in x_axis]
y2_axis = [round(random.uniform(1.0, 7.0), 1) for _ in x_axis]

fig,axs = plt.subplots(nrows=1, ncols=2)
fig.supylabel('Magnitude')
fig.supxlabel('Day')
axs[0].set_title('June 2024')
axs[1].set_title('June 2025')

axs[0].plot(x_axis, y1_axis, color='magenta')
axs[1].plot(x_axis, y2_axis)

plt.show()
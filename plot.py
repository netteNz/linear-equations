import matplotlib.pyplot as plt
import numpy as np

# plotting straight line y = mx + c
# where m is the slope and c the intercept

fig = plt.figure()
axis = fig.add_subplot(1, 1, 1)
x = np.linspace(-5, 5, 100)  # create evenly-spaced points
plt.title('Graph of Page 34')
axis.spines['left'].set_position('center')
axis.spines['bottom'].set_position('center')
axis.spines['right'].set_color('none')
axis.spines['top'].set_color('none')
axis.xaxis.set_ticks_position('bottom')
axis.yaxis.set_ticks_position('left')

plt.plot(x, 2*x+1, '-r', label='y=2x+1')
plt.plot(x, 2*x-1, '-g', label='y=2x-1')
plt.plot(x, x/2, '-b', label='y=x/2')
plt.plot(x, 3*x-2, '-k', label='y=3x-2')
plt.plot(x, 2*x+8, '-g', label='y=2x+8')
plt.legend(loc='upper left')

plt.plot()
plt.show()
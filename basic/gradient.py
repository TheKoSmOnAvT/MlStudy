import time
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*x - 5*x + 1

def df(x):
    return 2*x - 5

N = 20
xx = -10
lamd = 0.1

x_plt = np.arange(-50, 50.0, 0.1)
f_plt = [f(x) for x in x_plt]

plt.ion()
fig, ax = plt.subplots()
plt.grid(True)

ax.plot(x_plt, f_plt)
point = ax.scatter(xx, f(xx), c='red')

for i in range(N):
    xx = xx - df(xx)*lamd

    point.set_offsets([xx, f(xx)])
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.2)


plt.ioff()
print(xx)
ax.scatter(xx, f(xx), c ='blue')
plt.show()
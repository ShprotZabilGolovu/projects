from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def circle_move(R=0.5, t=0):
    x0 = R* np.cos(t)
    y0 = R* np.sin(t)
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = x0 + np.cos(alpha)
    y = y0 + np.sin(alpha)
    return x, y


fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')


def animate(i):
    ball.set_data(circle_move(t=i))
    return ball


edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=np.arange(-2, 2, 0.01), interval=30)
ani.save('animation_3.gif', writer="pillow")



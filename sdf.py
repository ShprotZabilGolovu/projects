from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def circle_move(R=0.5, t=0):
    x0 = R* np.cos(t)
    y0 = R* np.sin(t)
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = 3 * R * np.cos(alpha) ** 3 + x0
    y = 3 * R * np.sin(alpha) ** 3 + y0
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

ani = FuncAnimation(fig, animate, frames=np.arange(-3, 3, 0.01), interval=30)
ani.save('animation_3.gif', writer="pillow")



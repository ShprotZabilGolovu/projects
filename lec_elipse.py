from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def circle_move(a, b):
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = a*np.cos(alpha)
    y = b*np.sin(alpha)
    return x, y


fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='r', label='Ball')

frames = 100

def animate(i):
    ball.set_data(circle_move(1, 1-0.005*i))
    return ball


edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save('animation_3.gif', writer="pillow")
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def circle_move(R=1, t=0, beta=0):
    x0 = 0
    y0 = 0
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = x0 + R * np.cos(alpha) ** 3 
    y = y0 + R * np.sin(alpha) **3 
    
    x_1 = -R
    y_1 = 0
    X = x0 + (x - x_1) * np.cos(beta) - (y - y_1) * np.sin(beta)
    Y = y0 + (y - y_1) * np.cos(beta) + (x - x_1) * np.sin(beta) 
    return X, Y


fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='r', label='Ball')


def animate(i):
    ball.set_data(circle_move(R=1, beta=i))
    return ball


edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=np.arange(-3, 3, 0.01), interval=30)
ani.save('animation_3.gif', writer="pillow")



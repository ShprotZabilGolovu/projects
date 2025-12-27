from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def star(R=0.5,t=2):
    x = R*np.cos(t) ** 3
    y = R*np.sin(t) ** 3
    return x, y

fig, ax = plt.subplots()
zvezda, = plt.plot([], [], '-', color='r', label='Star')


def animate(t):
    zvezda.set_data(star(t=t))
    return zvezda


edge = 3
plt.axis('equal')
ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)

ani = FuncAnimation(fig, animate, frames=100, interval=30)
ani.save('svezdochka.gif', writer="pillow")


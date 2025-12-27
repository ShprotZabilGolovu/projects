import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

phi = np.linspace(-np.pi / 2,np.pi / 2, 100)
theta = np.linspace(0, 2 * np.pi, 100)

x = np.outer(phi, np.cos(theta))
y = np.outer(phi, np.sin(theta))
z = np.outer(phi ** 2, np.ones(len(theta)))

ax.plot_surface(x, y, z)

plt.savefig("paraboloid.png")
plt.close()


a = np.linspace(2, 6, 100)
b = np.linspace(7, 18, 100)
c = np.linspace(8, 20, 100)
x = a * np.outer(np.cos(phi), np.sinh(theta))
y = b * np.outer(np.sin(phi), np.sinh(theta))
z = c * np.outer(np.sinh(theta), np.ones(len(phi)))

ax.plot_surface(x, y, z)

plt.savefig("hyperboloid.png")
plt.close()
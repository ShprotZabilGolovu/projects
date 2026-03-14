import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d
import h5py
import sys


AE = 149597870700
N = 10000
M_SUN = 1.998e30
G = 6.67e-11

box_size = 100 * AE

masses = np.full(N, 1e17)
id_parts = np.arange(0, N, 1)

phi = np.linspace(0, 2*np.pi, N)
r = (np.random.random(N) * 1.2 + 2.1) * AE

x = r * np.cos(phi)
y = r * np.sin(phi)
z = np.zeros(N) 
z1 = np.zeros(N) + 0.1
z2 = np.zeros(N) - 0.1
z3 = np.zeros(N) + 0.2
z4 = np.zeros(N) - 0.2
coords = np.zeros((N, 3))
coords1 = np.zeros((N, 3))
coords2 = np.zeros((N, 3))
coords3 = np.zeros((N, 3))
coords4 = np.zeros((N, 3))
coords[:, 0], coords[:, 1], coords[:, 2] = x, y, z
coords1[:, 0], coords1[:, 1], coords1[:, 2] = x, y, z1
coords2[:, 0], coords2[:, 1], coords2[:, 2] = x, y, z2
coords3[:, 0], coords3[:, 1], coords3[:, 2] = x, y, z3
coords4[:, 0], coords4[:, 1], coords4[:, 2] = x, y, z4

coord = np.append(coords, coords1, coords2, coords3, coords4)


v = np.sqrt(G * M_SUN / r)
v_x = - v * np.sin(phi)
v_y = v * np.cos(phi)
v_z = np.zeros(N)
v_z1 = np.zeros(N) + 0.1 
v_z2 = np.zeros(N) - 0.1
v_z3 = np.zeros(N) + 0.2
v_z4 = np.zeros(N) - 0.2
print(v)
vel = np.zeros((N, 3))
vel1 = np.zeros((N, 3)) 
vel2 = np.zeros((N, 3)) 
vel3 = np.zeros((N, 3)) 
vel4 = np.zeros((N, 3)) 
vel[:, 0], vel[:, 1] = v_x, v_y
vel1[:, 0], vel1[:, 1] = v_x, v_y
vel2[:, 0], vel2[:, 1] = v_x, v_y
vel3[:, 0], vel3[:, 1] = v_x, v_y
vel4[:, 0], vel4[:, 1] = v_x, v_y


#Sun
masses[0] = M_SUN
coords[0] = [0, 0, 0]
vel[0] = [0, 0, 0]


coords = coords + box_size / 2
print(coords)

# plt.plot(coords[:, 0], coords[:, 1] , 'o', color='#FF3838')
# plt.axis('equal')
# plt.savefig('Solor_sys.png', dpi=1000)
# plt.close()


# File

file = h5py.File('./IC.hdf5', "w")

# Header
grp = file.create_group("/Header")
grp.attrs["BoxSize"] = box_size
grp.attrs["NumPart_Total"] = [0, N, 0, 0, 0, 0]
grp.attrs["NumPart_Total_HighWord"] = [0, 0, 0, 0, 0, 0]
grp.attrs["NumPart_ThisFile"] = [0, N, 0, 0, 0, 0]
grp.attrs["Time"] = 0.0
grp.attrs["NumFilesPerSnapshot"] = 1
grp.attrs["MassTable"] = [0.0, N, 0.0, 0.0, 0.0, 0.0]
grp.attrs["Flag_Entropy_ICs"] = 0
grp.attrs["Dimension"] = 3

# Units
grp = file.create_group("/Units")
grp.attrs["Unit length in cgs (U_L)"] = 100
grp.attrs["Unit mass in cgs (U_M)"] = 1000
grp.attrs["Unit time in cgs (U_t)"] = 1.0
grp.attrs["Unit current in cgs (U_I)"] = 1.0
grp.attrs["Unit temperature in cgs (U_T)"] = 1.0


# Particle group
grp = file.create_group("/PartType1")

ds = grp.create_dataset("Velocities", (N, 3), "f", data=vel)
ds = grp.create_dataset("Masses", (N, 1), "f", data=masses)
ds = grp.create_dataset("ParticleIDs", (N, 1), "L", data = id_parts)
ds = grp.create_dataset("Coordinates", (N, 3), "d", data=coord)

file.close()
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

from celestialobject import CelestialObject
from solarsystem import SolarSystem

solarsystem = SolarSystem(1.989e30, 84600)
solarsystem.add_celestial(mass=5.972e24,
                          location=np.array([150.46e9, 0]),
                          velocity=np.array([0, 29785.0]),
                          name='earth')
sun = []
earth = []

for i in range(1000):
    solarsystem.update(timestep=86400)
    sun.append(solarsystem.celestials[0].location)
    earth.append(solarsystem.celestials[1].location)
sun = np.array(sun)
earth = np.array(earth)

fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.scatter(earth[:, 0], earth[:, 1], c='blue', s=10)
ax.scatter(sun[:, 0], sun[:, 1], c='yellow', s=100)
plt.show()
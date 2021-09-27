import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

from celestialobject import CelestialObject
from solarsystem import SolarSystem

solarsystem = SolarSystem(1.989e30, 150000)
solarsystem.add_celestial(mass=5.972e24,
                          location=np.array([150.46e9, 0]),
                          velocity=np.array([0, 29785.0]),
                          name='earth')
solarsystem.add_celestial(mass=1e27, location=np.array([0, 200e9]),
                          velocity=np.array([35000,0]),
                          name='other_sun')
sun = []
earth = []
other_sun = []

for i in range(10000):
    solarsystem.update()
    sun.append(solarsystem.celestials[0].location)
    earth.append(solarsystem.celestials[1].location)
    other_sun.append(solarsystem.celestials[2].location)
sun = np.array(sun)
earth = np.array(earth)
other_sun = np.array(other_sun)

fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.scatter(earth[:, 0], earth[:, 1], c='blue', s=10)
ax.scatter(sun[:, 0], sun[:, 1], c='yellow', s=100)
ax.scatter(other_sun[:, 0], other_sun[:, 1], c='red', s=20)
plt.show()
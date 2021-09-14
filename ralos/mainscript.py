from celestialobject import CelestialObject
from solarsystem import SolarSystem
import matplotlib.pyplot as plt
import numpy as np

solarsystem = SolarSystem(1.989e30)
print(solarsystem.celestials)
solarsystem.add_celestial(mass=5.972e24,
                          location=np.array([150.46e9, 0]),
                          velocity=np.array([0, 29785.0]),
                          name='earth')

print(solarsystem.celestials)
sun = []
earth = []
for i in range(10000):
    solarsystem.update(timestep=86400)
    sun.append(solarsystem.celestials[0].location)
    earth.append(solarsystem.celestials[1].location)
sun = np.array(sun)
earth = np.array(earth)

plt.scatter(earth[:,0], earth[:,1], c='blue')
plt.scatter(sun[:,0], sun[:,1], c='yellow')
plt.show()
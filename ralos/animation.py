import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter

from celestialobject import CelestialObject
from solarsystem import SolarSystem

solarsystem = SolarSystem(1.989e30, 84600)
solarsystem.add_celestial(mass=5.972e24,
                          location=np.array([150.46e9, 0]),
                          velocity=np.array([0, 29785.0]),
                          name='earth')
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-180e9, 180e9)
ax.set_ylim(-180e9, 180e9)


def animate(i):
    solarsystem.update(timestep=86400)
    ax.plot(solarsystem.celestials[0].location[0], 
            solarsystem.celestials[0].location[1], 
            'yo')
    ax.plot(solarsystem.celestials[1].location[0], 
            solarsystem.celestials[1].location[1], 
            'bo')


FuncAnimation(fig, animate, frames=365)
plt.show() 
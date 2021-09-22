import numpy as np
from celestialobject import CelestialObject
from typing import List


class SolarSystem:
    def __init__(self,
                 sunmass: float,
                 interval: int):
        self._celestials = []
        self.interval = interval
        self.add_celestial(location=np.array([0, 0]),
                           mass=sunmass,
                           velocity=np.array([0, 0]),
                           name='sun')

    @property
    def celestials(self):
        return self._celestials

    @celestials.setter
    def celestials(self,
                   celestials: List['CelestialObject']):
        self._celestials = celestials

    def add_celestial(self,
                      location: np.array,
                      mass: float,
                      velocity: np.array,
                      name: str = None):
        celestial = CelestialObject(mass=mass,
                                    location=location,
                                    velocity=velocity,
                                    interval=self.interval,
                                    name=name)
        self.celestials.append(celestial)

    def update(self,
               timestep=1):
        # update the position for each celestial according to their position
        for celestial in self.celestials:
            celestial.update_location()

        for celestial in self.celestials:
            celestial.velocity_change(self.celestials)

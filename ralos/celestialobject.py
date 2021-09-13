import numpy as np
from typing import List


class CelestialObject:
    def __init__(self,
                 mass: float,
                 location: np.array,
                 velocity: np.array):
        self._mass = mass
        self._location = location
        self._velocity = velocity

    ################
    #  PROPERTIES  #
    ################

    @property
    def mass(self):
        return self._mass

    @property
    def velocity(self):
        return self._velocity

    @property
    def location(self):
        return self._location

    #############
    #  SETTERS  #
    #############

    @mass.setter
    def mass(self,
             mass: float):
        self._mass = mass

    @velocity.setter
    def velocity(self,
                 velocity: np.array):
        self._velocity = velocity

    @location.setter
    def location(self,
                 location: np.array):
        self._location = location

    ###############
    #  FUNCTIONS  #
    ###############

    def update_location(self,
                        interval: int = 1):
        self.location = self.location + (interval * self.velocity)

    def gravity_force(self,
                      celestial: 'CelestialObject'):
        G = 6.67408e-11
        m1 = self.mass
        m2 = celestial.mass
        rsquared = np.linalg.norm(self.location-celestial.location)**2
        if rsquared != 0:
            return G * m1 * m2 / rsquared
        else:
            return 0

    def all_forces(self,
                   celestials: List['CelestialObject']):
        forces = []
        for celestial in celestials:
            forces.append(self.gravity_force(celestial))
        return np.array(forces)

    def velocity_change(self,
                        celestials: List['CelestialObject']):
        forces = self.all_forces(celestials=celestials)
        total_force = np.sum(forces, axis=0)
        self.velocity = self.velocity + total_force

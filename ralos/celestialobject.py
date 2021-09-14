import numpy as np
from typing import List


class CelestialObject:
    def __init__(self,
                 mass: float,
                 location: np.array,
                 velocity: np.array,
                 interval: np.array,
                 name: str = None):
        self._mass = mass
        self._location = location
        self._velocity = velocity
        self._name = name
        self._interval = interval

    def __str__(self):
        return self._name

    ################
    #  PROPERTIES  #
    ################

    @property
    def interval(self):
        return self._interval
    
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
                 velocity: np.ndarray):
        self._velocity = velocity

    @location.setter
    def location(self,
                 location: np.ndarray):
        self._location = location

    ###############
    #  FUNCTIONS  #
    ###############

    def update_location(self):
        self.location = self.location + (self.interval * self.velocity)

    def gravity_force(self,
                      celestial: 'CelestialObject'):
        G = 6.67408e-11
        m1 = self.mass
        m2 = celestial.mass
        rsquared = np.linalg.norm(celestial.location - self.location)**2
        if rsquared != 0:
            g = G * m1 * m2 / rsquared
            normvector = (celestial.location - self.location)/np.linalg.norm(celestial.location - self.location)
            return normvector * g
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
        self.velocity = self.velocity + (total_force/self.mass)*self.interval

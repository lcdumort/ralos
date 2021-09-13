import numpy as np


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
                 velocity: (float, float)):
        self._velocity = velocity

    @location.setter
    def location(self,
                 location: (float, float)):
        self._location = location

    ###############
    #  FUNCTIONS  #
    ###############

    def update_location(self,
                        interval: int = 1):
        self.location = self.location + (interval * self.velocity) 
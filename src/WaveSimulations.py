__author__='Anne Oline Hågenvik'
__author_email__='haagenvik@icloud.com'

import matplotlib.pyplot as plt
import numpy as np
import time

class Wave:
    x = None
    y = None
    timesteps = None
    amplitude = 0
    wavelength = 0
    frequency = 0
    phase = 0
    kx = 0
    n_points = 1000

    def __init__(self, amplitude, wavelength, frequency, x_max, t_max):
        self.x=np.arange(x_max, step=x_max/self.n_points)
        self.timesteps=np.arange(t_max, step=t_max/self.n_points)
        self.amplitude = amplitude
        self.wavelength = wavelength
        self.frequency = frequency
        self.kx = 2*np.pi/wavelength

        return

    def plot_1d_wave(self):
        self.y = np.sin(self.kx*self.x + self.phase)
        plt.plot(self.x, self.y)
        plt.xlabel('x-aksen [enhet: m, nm, ...]')
        plt.ylabel('y-aksen [enhet: utslag, for eksempel elektrisk felt]')
        plt.show()

        return


if __name__ == "__main__":
    wave = Wave(amplitude=1, wavelength=10, frequency=0, x_max=100, t_max=1000)

    wave.plot_1d_wave()


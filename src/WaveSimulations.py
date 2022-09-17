__author__='Anne Oline Hågenvik'
__author_email__='haagenvik@icloud.com'

import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

class Bolge:
    x = None
    y = None
    tidssteg = None
    amplitude = 0
    bolgelengde = 0
    frekvens = 0
    bolgefart = 0
    refleksjonskoeffisient = 0
    fase = 0
    kx = 0
    n_punkt = 1000

    def __init__(self, amplitude, bolgelengde, frekvens, x_max, t_max, bolgefart=0, refleksjonskoeffisient=0):
        self.x=np.arange(x_max, step=x_max/self.n_punkt)
        self.timesteps=np.arange(t_max, step=t_max/self.n_punkt)
        self.amplitude = amplitude
        self.bolgelengde = bolgelengde
        self.frekvens = frekvens
        self.bolgefart = bolgefart
        self.kx = 2*np.pi/bolgelengde
        self.refleksjonskoeffisient = refleksjonskoeffisient

        return

    def plot_1d_bolge(self):
        self.y = np.sin(self.kx*self.x + self.fase)
        plt.plot(self.x, self.y)
        plt.xlabel('x-aksen [enhet: m, nm, ...]')
        plt.ylabel('y-aksen [enhet: utslag, for eksempel elektrisk felt]')
        plt.show()

        return
    
    
    def refleksjon(self):
        plt.rcParams["figure.figsize"] = [7.50, 3.50]
        plt.rcParams["figure.autolayout"] = True
        
        fig = plt.figure()
        ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
        line, = ax.plot([], [], lw=2)
        
        n1 = int(self.n_punkt/2)
        n2 = self.n_punkt
        
        x = np.linspace(0, 2, self.n_punkt)
        x1 = x[0:n1]
        x2 = x[n1:n2]
        
        A = self.amplitude
        v = self.bolgefart
        k = self.kx
        r = self.refleksjonskoeffisient
        
        
        def init():
           line.set_data([], [])
           return line,
        
        def animate(i):
                    
            y1 = A*np.sin(k * (x2 - v * i)) + r*A*np.sin(k * (x2 + v * i))
            y2 = (1-r)*A*np.sin(k * (x2 - v * i))
            
            y = np.append(y1, y2)
            
            line.set_data(x, y)
        
            return line,
        
        anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

        if r>0:
            plt.axvline(x = 1, color = 'k', label = 'axvline - full height')
        plt.show()
        
        return anim


if __name__ == "__main__":
    bolge = Bolge(amplitude=1, bolgelengde=0.25, frekvens=0, x_max=2, t_max=1000, bolgefart = 0.01, refleksjonskoeffisient=0.5)

    bolge.refleksjon()


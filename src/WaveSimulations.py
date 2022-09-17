#__author__='Anne Oline Hågenvik'
#__author_email__='haagenvik@icloud.com'

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
    brytningsindeks = 1
    fase = 0
    kx = 0
    n_punkt = 200

    def __init__(self, amplitude, bolgelengde, x_max, t_max, bolgefart=0):
        self.x=np.arange(x_max, step=x_max/self.n_punkt)
        self.timesteps=np.arange(t_max, step=t_max/self.n_punkt)
        self.amplitude = amplitude
        self.bolgelengde = bolgelengde
        self.frekvens = bolgefart/bolgelengde
        self.bolgefart = bolgefart
        self.kx = 2*np.pi/bolgelengde

        return

    def plot_1d_bolge(self):
        self.y = np.sin(self.kx*self.x + self.fase)
        plt.plot(self.x, self.y)
        plt.xlabel('x-aksen [enhet: m, nm, ...]')
        plt.ylabel('y-aksen [enhet: utslag, for eksempel elektrisk felt]')
        plt.show()

        return
    
    
    def bevegende_bolge(self):
        return self.refleksjon()
    
    
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
        
        if self.brytningsindeks != 1:
            brytningsindeks = self.brytningsindeks
            
            r = (1 - brytningsindeks)/(1+brytningsindeks)
            t = 2/(1+brytningsindeks)
        
        else:
            brytningsindeks = 1
            r = self.refleksjonskoeffisient
            t = (1-r)
        
        
        
        
        def init():
           line.set_data([], [])
           return line,
        
        def animate(i):
                    
            #y1 = A*np.sin(k * (x1 - v * i)) + r*A*np.sin(k * (x1 + v * i))
            #y2 = (1-r)*A*np.sin(k * (x2 - v * i))
            
            y1 = A*np.exp(1j*(k * (x1 - v * i))) + r*A*np.exp(-1j*(k * (x1 + v * i)))
            y2 = t*A*np.exp(1j*(k * (brytningsindeks*x2 - v * i)))
            
            
            y = np.append(y1, y2)
            
            line.set_data(x, np.real(y))
        
            return line,
        
        anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

        if self.refleksjonskoeffisient>0 or self.brytningsindeks != 1:
            plt.axvline(x = 1, color = 'k', label = 'axvline - full height')
        plt.show()
        
        return anim
    
    
    def brytning(self):
        plt.rcParams["figure.figsize"] = [7.50, 7.5]
        plt.rcParams["figure.autolayout"] = True
        
        n = self.n_punkt
        
        fig, ax = plt.subplots()
        
        x = np.linspace(-1,1, n)
        y = np.linspace(-2,2, n * 2)
        X, Y = np.meshgrid(x, y)
        
        
        n1 = int(n/2)
        n2 = n
        
        x1 = x[0:n1]
        x2 = x[n1:n2]
        
        A = self.amplitude
        v = self.bolgefart
        k = self.kx
        
        theta = np.pi/4
        
        kx = k*np.cos(theta)
        ky = k*np.sin(theta)
        
        if self.brytningsindeks != 1:
            brytningsindeks = self.brytningsindeks
            
            
            theta_t = np.arcsin(np.sin(theta)/brytningsindeks)
            
            r = (np.cos(theta) - brytningsindeks*np.cos(theta_t))/(np.cos(theta)+brytningsindeks*np.cos(theta_t))
            t = 2*np.cos(theta)/(np.cos(theta)+brytningsindeks*np.cos(theta_t))
        
        else:
            brytningsindeks = 1
            theta_t = theta
            r = self.refleksjonskoeffisient
            t = (1-r)
        
    
        kx_t = k*brytningsindeks*np.cos(theta_t)     
        
        A1 = np.zeros(X.shape)
        A2 = np.zeros(X.shape)
        
        A1[:, 0:n1] = A
        A2[:, n1:n2] = A
        
        G = (A1*(np.exp(1j*kx*X) + r*np.exp(-1j*kx*X)) + A2*t*np.exp(1j*kx_t*X))*np.exp(1j*ky*Y)
        cax = ax.pcolormesh(x, y, np.real(G[:-1, :-1]), vmin=-1, vmax=1, cmap='Blues')
        fig.colorbar(cax)
        
        def animate(i):
           cax.set_array(np.real(G[:-1, :-1]*np.exp(-1j*k*v*i)).flatten())
        
        anim = animation.FuncAnimation(fig, animate, interval=1, frames=200)
        #anim.save('517.gif')
        plt.show()
        
        

        if self.refleksjonskoeffisient>0 or self.brytningsindeks != 1:
            plt.axvline(x = 0, color = 'k', label = 'axvline - full height')
        plt.show()
        
        return anim
    
    


if __name__ == "__main__":
    bolge = Bolge(amplitude=1, bolgelengde=0.25, x_max=2, t_max=1000, bolgefart = 0.01)
    
    
    bolge.brytningsindeks = 1.33
    bolge.brytning()


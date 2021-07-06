
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Grapher:
    
    def __init__(self, data, sample_rate:float = 40):
        self.data = data
        self.sample_rate = sample_rate
        self.fig, self.ax = plt.subplots()
    
    def update_data(self, data):
        self.data = data
        
    def run(self):
        print("running graph")
        self.plotting_data, = self.ax.plot(0, self.data[0])
        self.anim = FuncAnimation(fig=self.fig, func=self.update_graph, interval=1.0/self.sample_rate, blit=True)
        plt.show()
        
    def update_graph(self, i):
        
        self.ax.cla()
        
        # plot the buffer
        x_values = np.arange(1, len(self.data)+1)/self.sample_rate
        self.ax.plot(x_values, self.data)

        # add attributes to axes
        self.ax.set_xlabel('time (s)')
        self.ax.set_ylabel('signal')
        self.ax.set_ylim(-0.25, 1.0)
        self.ax.set_xlim(0, len(self.data)/self.sample_rate)
        self.ax.set_title('Myoware Monitor')
        self.ax.grid()
        
        return self.ax.plot()
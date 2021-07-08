
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Grapher:
    
    def __init__(self, data, sample_rate=40.0, threshold=0.5):
        self.data = data
        self.sample_rate = sample_rate
        self.fig, self.ax = plt.subplots()
        self.threshold = threshold
        self.meetsThreshold = False
        
    def update_data(self, data):
        self.data = data
        
    def run(self):
        print("running graph")
        self.plotting_data, = self.ax.plot(0, self.data[0])
        self.anim = FuncAnimation(fig=self.fig, func=self.update_graph, interval=1000*1.0/self.sample_rate, blit=True)
        self.x_values = np.arange(1, len(self.data)+1) / self.sample_rate
        plt.show()
        
    def update_graph(self, i):
        
        self.ax.cla()
        
        # plot the threshold line and span
        plt.axhspan(0, self.threshold, color='lightblue', alpha=0.25)
        y_arr = np.repeat(self.threshold, len(self.x_values))
        self.ax.plot(self.x_values, y_arr, color='r')

        # plot the buffer, with the last second grayed out
        self.ax.plot(self.x_values, self.data, color='blue')
        
        # add attributes to axes
        self.ax.set_xlabel('time (s)')
        self.ax.set_ylabel('signal')
        self.ax.set_xlim(0, self.x_values[-1])
        self.ax.set_title('Myoware Monitor')
        self.ax.grid()
        
        # display feedback for contraction when applicable
        if self.meetsThreshold:
            y_pos = self.ax.get_ylim()[1] * 0.2
            self.ax.text(self.x_values[-1]*0.25, y_pos, 'MUSCLE CONTRACTION!', fontweight='bold',
                         fontsize=15, bbox={'facecolor':'red', 'alpha':0.9, 'pad':10})
        
        return self.ax.plot()

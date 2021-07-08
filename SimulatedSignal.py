import numpy as np
from threading import Timer, Event

class SimulatedSignal:
    
    def __init__(self, sample_rate = 40, cycle_duration = 2.0, autostart=True):
        self.sample_rate = sample_rate
        self.cycle_duration = cycle_duration # seconds
        self.elapsed_time: float = 0.0
        self.current_signal_value: float = 0.0
        self.timer_completed = Event()
        self.isRunning: bool = False
        if autostart:
            self.start()

    def start(self):
        self.timer_completed.clear()
        Timer(1.0/self.sample_rate, self.calculate_current_datapoint).start()
        self.isRunning = True
        
    def stop(self):
        self.timer_completed.set()
        self.isRunning = False
    
    def calculate_current_datapoint(self):
        # loops a simple sine function
        if not self.timer_completed.is_set():
            value = np.sin(self.elapsed_time * (1/self.cycle_duration * (2 * np.pi)))
            if value < 0:
                value = 0
            self.elapsed_time += 1.0/self.sample_rate
            
            Timer(1.0/self.sample_rate, self.calculate_current_datapoint).start()
            
            self.current_signal_value = value
        else:
            self.current_signal_value = -1.0
            self.isRunning = False
        
    # for external classes to sample the current value
    def read(self) -> float:
        return self.current_signal_value

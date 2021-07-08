
from ArduinoService import ArduinoService
import numpy as np
import collections
from threading import Timer
from Grapher import Grapher

'''
main.py

Myoware Monitor is a tutorial application that receives serial data from a Myoware sensor
connected to an Arduino via PySerial, stores the incoming data to a buffer and graphs
it using matplotlib.

A simulator signal (sin wave) is also available to show how the python side works without
having an active serial connection.

'''

if __name__ == '__main__':
    
    print("Myoware Monitor tutorial")
    
    max_samples_on_graph = 200
    buffer = collections.deque(np.zeros(max_samples_on_graph))

    # start the Arduino Live/Simulated interface
    arduino = ArduinoService()
    
    # start matplotlib object
    grapher = Grapher(data=buffer, sample_rate = arduino.simulator.sample_rate)
    
    def add_value_to_buffer():
        buffer.append(arduino.read())
        buffer.popleft()
        grapher.update_data(buffer)
        
        Timer(1.0/arduino.simulator.sample_rate, add_value_to_buffer).start()
        
    # loop the buffer update
    Timer(1.0/arduino.simulator.sample_rate, add_value_to_buffer).start()
    
    grapher.run()

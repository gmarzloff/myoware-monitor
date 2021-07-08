'''
ArduinoService.py

Arduino Service manages the serial reading from Arduino.

'''

import serial
from SimulatedSignal import SimulatedSignal

class ArduinoService:
    
    def __init__(self, port='COM4', baudrate=115200):
    
        print("Attempting to connect to serial device on port " + port)
        try:
            self.ser = serial.Serial(port=port, baudrate=baudrate, timeout=0.1)
            print("SUCCESS: Serial device is connected.")
        except serial.serialutil.SerialException:
            print("Warning: Arduino not connected. Starting simulated signal...")
            self.simulator = SimulatedSignal()
            
    def read(self):
        if self.simulator.isRunning:
            return self.simulator.read()
        else:
            return self.ser.readline()
    
    def close(self):
        self.ser.close()

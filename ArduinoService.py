'''
ArduinoService.py

Arduino Service manages the serial reading from Arduino.

'''

import serial


class ArduinoService:
    
    def __init__(self, port='COM4', baudrate=115200):
    
        print("Attempting to connect to serial device on port %s", port)
        try:
            self.ser = serial.Serial(port=port, baudrate=baudrate, timeout=0.1)
            print("SUCCESS: Serial device is connected.")
        except serial.serialutil.SerialException:
            print("FAILED: Arduino not connected")
        
    def read(self):
        return self.ser.readline()
    
    def close(self):
        self.ser.close()

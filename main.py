
import serial
from ArduinoService import ArduinoService

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
    
    arduino = ArduinoService()

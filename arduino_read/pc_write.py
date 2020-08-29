import serial
import time
arduino = serial.Serial('/dev/ttyACM0', 9600)

while True:
    arduino.write(b'sending data to arduino from PC')
    
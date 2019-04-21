import time
import serial

ser = serial.Serial('/dev/ttyUSB0', baudrate=57600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
def poke():
    ser.write(b'2b')
    
def rapid_poke():
    ser.write(b'4b')
    
def move_finger(x):
    string_x=str(x)
    ser.write(bytes(string_x, 'ascii'))
    ser.write(b'a')
import serial
import os
import time as t
# "COM11" is the port that your Arduino board is connected.set it to port that your are using
ser = serial.Serial("/dev/ttyACM0", 9600)
while True:
    cc=str(ser.readline())
    print("Current Temperature .. ",cc[2:][:-5])
    os.system("python regressionRedo.py "+cc[2:][:-5])
    os.system("python testFinal.py "+cc[2:][:-5])
    t.sleep(3)

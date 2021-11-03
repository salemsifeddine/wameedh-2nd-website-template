
import serial

def arduino():
    sr=serial.Serial("com4",9600)
    arduino = sr.readline()
    dataarduino = str(arduino[0:len(arduino)].decode("utf-8"))
    realdata=dataarduino
    return realdata

while True:
    realdataarduino =  arduino()
    print(realdataarduino)
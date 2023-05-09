import os
import can 

os.system('sudo ip link set can0 type can bitrate 100000')
os.system('sudo ifconfig can0 up')

can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native

while 1:
    message = can0.recv(10.0)
    print(message)

    if message is None:
        print('Timeout occurred, no message.')

os.system('sudo ifconfig can0 down')
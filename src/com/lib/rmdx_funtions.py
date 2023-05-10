import can
import os
import time
from configs import CaptureConfigs as cf

def __init__(self,identifier):
    self.bus = None
    self.identifier = identifier


def setup(self):
    #----------------- setup can ------------------------------
    try:
        os.system('sudo /sbin/ip link set can0 up type can bitrate 1000000')
        #os.system('sudo ifconfig can0 up')
        time.sleep(0.1)
    except Exception as e:
        print(e)
    
    try:
        #can conection config
        bus = can.interface.Bus(bustype = 'socketcan',channel = 'can0')# socketcan_native
    except OSError:
        print('err: PiCAN board was not found')
        exit()
    except Exception as e:
        print(e)

    self.bus = bus
    return self.bus




def sendMessToMotor(self,motor_id,data_command):

    
    # ----------------- send data to motor ---------------------
    #define message
    #can_id = 0x142 #can direction 140 + motor ID
    #data = [0x31, 0x00, 0x04, 0x01, 0x04, 0x01, 0x04, 0x01] #variables PID
    #data= [0x81, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00] #apagar motor
    #data= [0x88, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00] #encender
    #data = [0xA1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00] #torque
    #data= [0xA2, 0x00, 0x00, 0x00,0x64, 0x64, 0x64, 0x64] #speed control

    can_id = motor_id
    data = data_command


    msg = can.Message(arbitration_id=can_id,data=data, is_extended_id=False)
    #send message
    self.bus.send(msg)
    time.sleep(0.1)
    print("MENSAJE: " + str(msg.data) )

    # ------------------ read message ----------------------
    receive_message = self.bus.recv(10.0)
    if receive_message is None:
        print('Timeout occurred, no message.')
        os.system('sudo /sbin/ip link set can0 down')
        
    os.system('sudo /sbin/ip link set can0 down')
    print("MENSAJE RECIVIDO : " + str(receive_message.data))
    


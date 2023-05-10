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

# -------- sends command -------------------------


def sendToSingleMotor(self,motor_id,data_command):
    # ----------------- send data to motor ---------------------
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

#def sendToMultiMotor(self,motor_id)

# ------ main commands ------------------
def stopMotor(self):
    
    
# ----- current(torque) -----------------



# ----- speed ---------------------------
# ----- position ------------------------
# ----- encoder -------------------------
# ----- error ---------------------------
# ----- aceleration ---------------------

import can
import os



def sendMessToMotor():
    os.system('sudo ip link set can0 type can bitrate 100000')
    os.system('sudo ifconfig can0 up')
    #can conection config
    can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')# socketcan_native
    #define message
    can_id = 0x141 #can direction  + motor ID
    data = [0x30,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
    msg = can.Message(arbitration_id=can_id,data=data)
    #send message
    can0.send(msg)
    print("MENSAJE: enviado " )
    os.system('sudo ifconfig can0 down')

if __name__ == "__main__":
    sendMessToMotor()

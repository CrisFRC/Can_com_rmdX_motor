import can
import os
import time


def sendMessToMotor():

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

    # ----------------- send data to motor ---------------------
    #define message
    can_id = 0x142 #can direction 140 + motor ID
    #data = [0x32, 0x00, 0x32, 0x32, 0x64, 0x32, 0x64, 0x64]
    data = [0xA1, 0x00, 0x00, 0x00, 0x64, 0x64, 0x00, 0x00]
    
    msg = can.Message(arbitration_id=can_id,data=data, is_extended_id=False)
    #send message
    bus.send(msg)
    time.sleep(0.1)
    print("MENSAJE: " + str(msg.data) )

    # ------------------ read message ----------------------
    receive_message = bus.recv(10.0)
    if receive_message is None:
        print('Timeout occurred, no message.')
        os.system('sudo /sbin/ip link set can0 down')
        
    os.system('sudo /sbin/ip link set can0 down')
    print("MENSAJE RECIVIDO : " + str(receive_message.data))
    

if __name__ == "__main__":
    sendMessToMotor()

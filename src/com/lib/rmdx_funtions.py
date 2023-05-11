import can
import os
import time
import configparser
from pathlib import Path
import os


# ------ utils --------------------------
def getDataHex(data):

    if "," in data:
        data = data.split(',')
        data_send = []
        for value in data:
            data_send.append(int(value, 16))
        return data_send
    else:
        return int(data, 16)


def getValueConfig(header, param):
    path = Path(__file__)
    ROOT_DIR = path.parent.absolute()
    config_path = os.path.join(ROOT_DIR, "comands.properties")
    config = configparser.RawConfigParser()
    config.read(config_path)
    return getDataHex(config.get(header, param))


class RMDX:

    def __init__(self):
        self.bus = None
        self.header = 'codeTypeAccionHex'
        # self.auto = self.getValueConfig(self.header,'util.null')

    def setup(self):
        # ----------------- setup can ------------------------------
        try:
            os.system('sudo /sbin/ip link set can0 up type can bitrate 1000000')
            # os.system('sudo ifconfig can0 up')
            time.sleep(0.1)
        except Exception as e:
            print(e)

        try:
            # can connection config
            bus = can.interface.Bus(bustype='socketcan', channel='can0')  # socketcan_native
        except OSError:
            print('err: PiCAN board was not found')
            exit()
        except Exception as e:
            print(e)

        self.bus = bus
        return self.bus

    # -------- sends command -------------------------

    def sendToMotor(self, motor_id, data_command):
        # ----------------- send data to motor ---------------------
        can_id = motor_id
        data = data_command
        msg = can.Message(arbitration_id=can_id, data=data, is_extended_id=False)
        # send message
        self.bus.send(msg)
        time.sleep(0.1)
        print("MENSAJE: " + str(msg.data))

        # ------------------ read message ----------------------
        receive_message = self.bus.recv(10.0)
        if receive_message is None:
            print('Timeout occurred, no message.')
            os.system('sudo /sbin/ip link set can0 down')

        os.system('sudo /sbin/ip link set can0 down')
        print("MENSAJE RECIVIDO : " + str(receive_message.data))
        return receive_message

    # def sendToMultiMotor(self,motor_id)

    # ------ main commands ------------------
    def stopMotor(self, motor_id):
        param = 'motor.stop'
        command = getValueConfig(self.header, param)
        message = [command, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        return self.sendToMotor(motor_id, message)

    def runMotor(self,motor_id):
        param = 'motor.run'
        command = getValueConfig(self.header,param)
        message = [command, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        return self.sendToMotor(motor_id, message)

    def offMotor(self,motor_id):
        param = 'motor.off'
        command = getValueConfig(self.header,param)
        message = [command, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        return self.sendToMotor(motor_id, message)

    # ----- current(torque) -----------------

    # ----- speed ---------------------------
    def speedClosedLoop(self, motor_id, data):
        param = 'send.speed'
        command = getValueConfig(self.header, param)
        message = [command, 0x00, 0x00, 0x00,
                   data[0], data[1], data[2], data[3]]
        return self.sendToMotor(motor_id, message)

    # ----- position ------------------------
    def setPositionClosedLoop(self, motor_id, data):
        param = 'send.position'
        command = getValueConfig(self.header, param)
        message = [command, 0x00, 0x00, 0x00,data[0], data[1], data[2], data[3]]
        return self.sendToMotor(motor_id,message)

    # ----- encoder -------------------------
    # ----- error ---------------------------
    # ----- aceleration ---------------------




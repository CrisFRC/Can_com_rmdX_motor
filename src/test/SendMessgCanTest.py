
import unittest
from com.lib import rmdx_funtions  as rmdx
from com.configs import CaptureConfigs as cf

class SendMess(unittest.TestCase):
    def send_mess_can(self):
        header = 'codeTypeAccionHex'
        param = 'send.torque'
        data = cf.getValueConfig(header,param)
        data_goal = [0xA1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.assertAlmostEqual(data,data_goal)


if __name__ == "__main__":
    unittest.main
#--------------------------------------------


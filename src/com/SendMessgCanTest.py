
import unittest
from lib import rmdx_funtions  as rmdx
import configs.CaptureConfigs as cf

class SendMess(unittest.TestCase):

    def test_get_properties(self):
        header = 'codeTypeAccionHex'
        param = 'send.torque'
        data = cf.getValueConfig(header,param)
        data_goal = [0xA1, 0x00, 0x00]
        print(data)
        self.assertEqual(data,data_goal)
        

if __name__ == "__main__":
    unittest.main()
#--------------------------------------------


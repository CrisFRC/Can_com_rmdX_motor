
import unittest
from lib import rmdx_funtions  as rmdx
import configs.CaptureConfigs as cf

class SendMess(unittest.TestCase):

    def test_get_properties(self):
        header = 'codeTypeAccionHex'
        param = 'send.torque'
        data = rmdx.getValueConfig(header,param)
        data_goal = 0xA1
        print(data)
        self.assertEqual(data,data_goal)

    def test_stop_motor(self):
        rmdx.setup()
        motor_id = 0x142
        res = rmdx.stopMotor(motor_id)
        #self.assertIsNotNone(res, "the data doesn't have to be null")
        

if __name__ == "__main__":
    unittest.main()
#--------------------------------------------


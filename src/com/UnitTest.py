
import unittest
from lib.rmdx_funtions  import RMDX  


class TestCommands(unittest.TestCase):

    def test_get_properties(self):
        rmdx = RMDX()
        header = 'codeTypeAccionHex'
        param = 'send.torque'
        data = getValueConfig(header,param)
        data_goal = 0xA1
        print(data)
        self.assertEqual(data,data_goal)

    def test_stop_motor(self):
        rmdx =  RMDX()
        rmdx.setup()
        motor_id = 0x142
        res = rmdx.stopMotor(motor_id)
        self.assertIsNotNone(res, "the data doesn't have to be null")
    
    def test_send_speed(self):
        rmdx = RMDX()
        rmdx.setup()
        motor_id = 0x142
        data = [0x00,0x00,0x00,0x00]
        res = rmdx.speedClosedLoop(motor_id,data)
        self.assertIsNotNone(res, "the data doesn't have to be null")


if __name__ == "__main__":
    unittest.main()
#--------------------------------------------


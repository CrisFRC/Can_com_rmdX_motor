
import unittest
from com.Send import sendMessToMotor

class SendMess(unittest.TestCase):
    def send_mess_can(self):
        sendMessToMotor()
        self.assertAlmostEqual(True,True)


if __name__ == "__main__":
    unittest.main
#--------------------------------------------


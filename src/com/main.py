import lib.rmdx_funtions as rmdx
from configs import CaptureConfigs as cf



if __name__ == "__main__":
    
#   read command param
    header = 'codeTypeAccionHex'
    param = 'send.torque'
    data = cf.getValueConfig(header,param)
    print(data)


    
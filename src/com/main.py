import lib.rmdx_funtions as rmdx
import configs.CaptureConfigs as cf



if __name__ == "__main__":
    
#   read command param
    header = 'codeTypeAccionHex'
    param = 'send.torque'
    data = cf.getValueConfig(header,param)
    print(data)


    
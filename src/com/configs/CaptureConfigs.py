import configparser
from pathlib import Path
import os


def getValueConfig(header,param):
    path = Path(__file__)
    ROOT_DIR = path.parent.absolute()
    config_path = os.path.join(ROOT_DIR, "config.properties")
    config = configparser.RawConfigParser()
    config.read(config_path)
    return getDataHex(config.get(header,param))

def getDataHex(data):


    if len(data) > 1:
        data = data.split(',')
        data_send =  []
        for value in data:
            data_send.append(int(value,16))
        return data_send
    else:
        return int(data,16)


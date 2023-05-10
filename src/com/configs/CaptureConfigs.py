import configparser


def getValueConfig(header,param):
    config = configparser.RawConfigParser()
    config.read("config.properties")
    return config.get(header,param)

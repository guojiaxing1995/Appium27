import yaml

class OperateYaml:
    def __init__(self,path=None):
        if path == None:
            self.stream = open('../config/devices.yaml','a+')
        else:
            self.stream = open(path)

    def read_yaml(self):
        data = yaml.load(self.stream)
        return data

    def get_devices(self,key):
        data = self.read_yaml()
        return data[key]

    def write_yaml(self,data):

        yaml.dump(data,self.stream)

    def join_devices_data(self,i,device,bp,port):
        data = {
            "device_info_" + str(i): {
                "deviceName": device,
                "bp": bp,
                "port": port
            }
        }
        return data

    def get_cloumn(self):

        return len(self.read_yaml())

    def clear_data(self):
        self.stream.truncate()


    def close_data(self):
        self.stream.close()
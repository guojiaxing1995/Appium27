#coding=utf-8
from doc_cmd import DosCmd
from port import Port
import threading
from OperateYaml import OperateYaml
import time

class Server:

    def __init__(self):
        self.dos = DosCmd()
        self.operateYaml = OperateYaml()
        self.command_list = self.create_command()


    def get_devices(self):
        '''获取设备信息'''
        devices_list = []
        result_list = self.dos.excute_cmd_result('adb devices')
        if len(result_list)>=3:
            for i in result_list:
                if '\tdevice' in i:
                    devices_list.append(i.split('\t')[0])

        return devices_list

    def create_command(self):
        port = Port()
        #appium -p 4700 -bp 4701 -U DU2TAN149P079327
        command_list = []
        device_list = self.get_devices()
        appium_port_list = port.create_port_list(4700,device_list)
        bootstrap_port_list = port.create_port_list(4900,device_list)
        for i in range(len(device_list)):
            now = time.strftime('%Y-%m-%d-%H_%M_%S')
            command = "appium -p "+str(appium_port_list[i])+" -bp "+str(bootstrap_port_list[i])+" -U "+device_list[i]+" --no-reset --session-override --log D:/PycharmProjects/Appium27/log/"+device_list[i]+str(now)+".log"
            command_list.append(command)
            self.operateYaml.clear_data()
            self.operateYaml.write_yaml(self.operateYaml.join_devices_data(i,device_list[i],str(bootstrap_port_list[i]),str(appium_port_list[i])))
        return command_list

    def start_server(self,i):
        self.start_list = self.command_list
        self.dos.excute_cmd(self.start_list[i])

    def kill_server(self):
        server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
        if server_list:
            self.dos.excute_cmd('taskkill -F -PID node.exe')


    def main(self):
        self.kill_server()
        for i in range(len(self.command_list)):
            appium_start = threading.Thread(target=self.start_server,args=(i,))
            appium_start.start()



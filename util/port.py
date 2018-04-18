#coding=utf-8
from doc_cmd import DosCmd

class Port:
    def port_is_used(self,port_num):
        '''检测端口是否被占用'''
        flag = None
        dos = DosCmd()
        result = dos.excute_cmd_result('netstat -ano | findstr ' + str(port_num))
        if result:
            flag = True
        else:
            flag = False
        return flag

    def create_port_list(self,start_port,device_list):
        '''生成可用端口'''
        port_list = []
        if device_list:
            while len(port_list) !=len(device_list):
                if self.port_is_used(start_port) !=True:
                    port_list.append(start_port)
                start_port = start_port + 1

            return port_list




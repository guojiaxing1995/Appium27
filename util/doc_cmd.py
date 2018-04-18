#coding=utf-8
import os

class DosCmd:
    def excute_cmd_result(self,command):
        result = os.popen(command).readlines()
        return result

    def excute_cmd(self,command):
        os.system(command)


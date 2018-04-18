#coding=utf-8
import ConfigParser

#'D:\PycharmProjects\Appium27\config\LocalElement.ini'

class ReadIni():
    def __init__(self,path=None):
        self.read_ini = ConfigParser.ConfigParser()
        if path==None:
            self.read_ini.read('D:\PycharmProjects\Appium27\config\LocalElement.ini')
        else:
            self.read_ini.read(path)

    def get_value(self,section,option):
        try:
            return self.read_ini.get(section, option)
        except:
            return None

readini = ReadIni()
print(readini.get_value('login_element','pass1word'))
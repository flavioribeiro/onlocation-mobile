'''
Created on 05/08/2010

@author: Wyll
'''

class Usuario(object):

    def __init__(self, plogin, psenha, pLocal):
        self.login = plogin
        self.senha = psenha
        self.local = pLocal

    def get_login(self):
        return self.__login


    def get_senha(self):
        return self.__senha


    def get_local(self):
        return self.__local


    def set_login(self, value):
        self.__login = value


    def set_senha(self, value):
        self.__senha = value


    def set_local(self, value):
        self.__local = value

    login = property(get_login, set_login, None, None)
    senha = property(get_senha, set_senha, None, None)
    local = property(get_local, set_local, None, None)
        
    
        
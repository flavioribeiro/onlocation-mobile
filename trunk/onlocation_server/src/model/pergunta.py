'''
Created on 07/08/2010

@author: Wyll
'''

class Pergunta(object):


    def __init__(self, pLocal, pQuestion, pUsuario):
        self.local = pLocal
        self.question = pQuestion
        self.usuario = pUsuario

    def get_local(self):
        return self.__local


    def get_question(self):
        return self.__question


    def get_usuario(self):
        return self.__usuario


    def set_local(self, value):
        self.__local = value


    def set_question(self, value):
        self.__question = value


    def set_usuario(self, value):
        self.__usuario = value

    local = property(get_local, set_local, None, None)
    question = property(get_question, set_question, None, None)
    usuario = property(get_usuario, set_usuario, None, None)
        
        
        
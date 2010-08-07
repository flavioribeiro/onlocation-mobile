'''
Created on 07/08/2010

@author: Wyll
'''

class Resposta(object):


    def __init__(self, pResp):
        self.resposta = pResp

    def get_resposta(self):
        return self.__resposta


    def set_resposta(self, value):
        self.__resposta = value

    resposta = property(get_resposta, set_resposta, None, None)
        
'''
Created on 04/08/2010

@author: Wyll
'''

import sys
import cherrypy
import pgdb
import os.path
from cherrytemplate import cherrytemplate, renderTemplate
from util import templateUtil
from model import usuario


class OnLocationServer(object):
    
    def __init__(self):
        self.conn = pgdb.connect(dsn = None, user = 'postgres', password = '62743233', host = 'localhost', database = 'onlocationdb')
        cherrytemplate.defaultOutputEncoding = 'UTF-8'
        cherrytemplate.defaultInputEncoding = 'latin-1'
        cherrytemplate.defaultTemplateDir = ''
        self.id = 0
        self.usuarios = {}
        self.messages = ''
    
    @cherrypy.expose
    def index(self):
        index = renderTemplate(file = 'pages/index.html')
        formLogin = renderTemplate(file = 'pages/formLogin.html')
        response = templateUtil.addContent(index, formLogin)
        return response
        
    
    @cherrypy.expose
    def default(self):
        return renderTemplate(file = 'pages/index.html')
    
    @cherrypy.expose
    def doLogin(self, pNome):
        self.id += 1
        user = usuario.Usuario(self.id, pNome)
        self.usuarios[self.id] = user
        
        cherrypy.session['user'] = user
        
        raise cherrypy.HTTPRedirect('/onlocation/doChat')
    
    @cherrypy.expose
    def doChat(self, pMsg = None):
        
        user = cherrypy.session.get('user')
        
        if pMsg == None:
            self.messages += user.get_login() + ' diz: Oi!!! <br>'
        else:
            self.messages += user.get_login() + ' diz: ' + pMsg + '<br>'
        
        msgArea = '<p>' + self.messages + '</p>'
        
        index = renderTemplate(file = 'pages/index2.html')
        formMsg = renderTemplate(file = 'pages/chat.html')
        
        response = templateUtil.addContent(index, msgArea + formMsg)
        
        return response
        
        

sys.path.append('src')
current_dir = os.path.dirname(os.path.abspath(__file__))

conf = {'/':{'tools.sessions.on':True,'tools.sessions.timeout':60},
        'global':{'server.socket_port': 8084,'log.error_file': "onlocation.log"},
        'databases':{'driver':'postgres','host':'localhost','port':5432},
        '/geral.css':{'tools.staticfile.on':True,'tools.staticfile.filename':current_dir +'/css/geral.css'}}

cherrypy.root = OnLocationServer()
cherrypy.quickstart(OnLocationServer(),'/onlocation', config=conf)
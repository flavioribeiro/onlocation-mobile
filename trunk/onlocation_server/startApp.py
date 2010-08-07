'''
Created on 04/08/2010

@author: Wyll
'''

import sys
import cherrypy
import pgdb
import os.path
from cherrytemplate import cherrytemplate, renderTemplate


class OnLocationServer(object):
    
    def __init__(self):
        self.conn = pgdb.connect(dsn = None, user = 'postgres', password = '62743233', host = 'localhost', database = 'onlocationdb')
        cherrytemplate.defaultOutputEncoding = 'UTF-8'
        cherrytemplate.defaultInputEncoding = 'latin-1'
        cherrytemplate.defaultTemplateDir = ''

        
    
    @cherrypy.expose
    def index(self):
        return renderTemplate(file = 'pages/index.html')
    
    @cherrypy.expose
    def default(self):
        return renderTemplate(file = 'pages/index.html')

sys.path.append('src')
current_dir = os.path.dirname(os.path.abspath(__file__))

conf = {'global':{'server.socket_port': 8084,'log.error_file': "onlocation.log"},
        'databases':{'driver':'postgres','host':'localhost','port':5432},
        '/geral.css':{'tools.staticfile.on':True,'tools.staticfile.filename':current_dir +'/css/geral.css'}}

cherrypy.root = OnLocationServer()
cherrypy.quickstart(OnLocationServer(),'/onlocation', config=conf)
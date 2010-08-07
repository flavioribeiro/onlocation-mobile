'''
Created on 04/08/2010

@author: Wyll
'''

import sys
import cherrypy
import pgdb
from cherrytemplate import cherrytemplate, renderTemplate

sys.path.append('src')

conf = {'global':{'server.socket_port': 8084,'log.error_file': "onlocation.log"},
        'databases':{'driver':'postgres','host':'localhost','port':5432}}
    
class OnLocationServer(object):
    
    def __init__(self):
        self.conn = pgdb.connect(dsn = None, user = 'postgres', password = '62743233', host = 'localhost', database = 'onlocationdb')
        cherrytemplate.defaultOutputEncoding = 'UTF-8'
        cherrytemplate.defaultInputEncoding = 'latin-1'
        cherrytemplate.defaultTemplateDir = ''

        
    
    @cherrypy.expose
    def index(self):
        return renderTemplate(file = 'pages/index.html')
    
cherrypy.root = OnLocationServer()
cherrypy.config.update(conf)
cherrypy.quickstart(OnLocationServer())
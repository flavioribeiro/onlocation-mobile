'''
Created on 04/08/2010

@author: Wyll
'''

import cherrypy
import pgdb

conf = {'global':{'server.socket_port': 8084,'log.error_file': "onlocation.log"},
        'databases':{'driver':'postgres','host':'localhost','port':5432}}

class Home(object):


    def __init__(self):
        self.conn = pgdb.connect(dsn = None, user = 'postgres', password = '62743233', host = 'localhost', database = 'onlocationdb')
        
    
    @cherrypy.expose
    def index(self):
        
        adr = self.conn.cursor()
        
        adr.execute("select * from teste")
        rows = adr.fetchall ()
        
        t = ''
        for i in (rows):
            t += str(i[0]) + ' ' + str(i[1]) + '<br>' 
            
        return t
        
cherrypy.config.update(conf)
cherrypy.quickstart(Home())

'''
Created on 04/08/2010

@author: Wyll
'''

import pgdb

class DAO(object):


    def __init__(self):
        self.conn = pgdb.connect(None, 'postgres', 62743233, 'localhost', 'onlocationdb')

    def get_conn(self):
        return self.__conn


    def set_conn(self, value):
        self.__conn = value

    conn = property(get_conn, set_conn, None, None)

        
    
        
        
'''
Created on 04/08/2010

@author: Wyll
'''

import pgdb

class Banco(object):


    def __init__(self):
        self.conn = pgdb.connect(None, 'postgres', 62743233, 'localhost', 'onlocationdb')
        
    
        
        
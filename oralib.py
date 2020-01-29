# -*- coding: utf-8 -*-
import cx_Oracle
import logging
from secrets import user,passwd,host,port,sid
logger = logging.getLogger('root')

class ora_lib(object):

    def __enter__(self):
        dsn_tns = cx_Oracle.makedsn(host, port, sid)
        try:
            self.__db = cx_Oracle.connect(user,passwd,dsn_tns)
            self.__cursor = self.__db.cursor()
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            if error.code == 1017:
                logger.error('Please check your credentials.')
            else:
                logger.error("Database connection error: {}".format(e.message))
            raise
        return self

    def __exit__(self,type,value,traceback):
        try:
            self.__cursor.close()
            self.__db.close()
        except:
            logger.error("Database Close Error")
            pass

    

            
            


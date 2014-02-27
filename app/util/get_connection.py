#import MySQLdb
#import MySQLdb.cursors
import sqlite3
from ..config import sqlitedb

def setup():
    #return MySQLdb.connect(host = mysql['host'],
    #                       user = mysql['user'],
    #                       passwd = mysql['password'],
    #                       db = mysql['db'],
    #                       port = mysql['port'],
    #                       cursorclass = MySQLdb.cursors.DictCursor)
    return sqlite()

def sqlite():
    conn = sqlite3.connect(sqlitedb)
    conn.row_factory = sqlite3.Row
    conn.text_factory = str
    return conn

import MySQLdb as mdb
import sys
import server

xk = mdb.connect(read_default_file='./.conf.cnf');


def insert(msg):
    with con:
        cur = xk.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS\
                     Jobs(Id INT PRIMARY KEY AUTO_INCREMENT,\
                          Task VARCHAR(25),\
                          Time TIMESTAMP)")
        cur.execute("INSERT INTO Jobs(Task) VALUES(msg)")


def outg():
    with xk:
        cur = xk.cursor()
        ki = int(cur.execute("SELECT LAST_INSERT_ID()"))
    return (ki)

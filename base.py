import MySQLdb as mdb
import sys
import server
import connection as xk
con = mdb.connect(read_default_file='./.conf.cnf');


def insert(msg):
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS\
                     Jobs(Id INT PRIMARY KEY AUTO_INCREMENT,\
                     Task VARCHAR(25),\
                     Time TIMESTAMP)")
        cur.execute("INSERT INTO Jobs(Task) VALUES(msg)")


def outg():
    with con:
        cur = con.cursor()
        ki = int(cur.execute("SELECT LAST_INSERT_ID()"))
    return (ki)

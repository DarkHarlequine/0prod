import ConfigParser
import sys
import MySQLdb as mdb

config = ConfigParser.RawConfigParser()
config.read('conf.cnf')
defhost = config.get("MySQLopts", "host")
defuser = config.get("MySQLopts", "user")
defpasswd = config.get("MySQLopts", "passwd")
defbase = config.get("MySQLopts", "base")
ruser = config.get("CRopts", "user")
rpasswd = config.get("CRopts", "passwd")
rhost = config.get("CRopts", "host")
konnekt = mdb.connect(rhost, ruser, rpasswd)
with konnekt:
    cur0 = konnekt.cursor()
    cur0.execute("CREATE DATABASE IF NOT EXISTS %s;\
                 CREATE USER '%s'@'%s' IDENTIFIED BY '%s';" % \
                 (defbase, defuser, defhost, defpasswd))
    cur0.close()
    cur1 = konnekt.cursor()
    cur1.execute("USE %s;\
                 GRANT ALL ON %s.* TO '%s'@'%s';" % \
                 (defbase, defbase, defuser, defhost))
    cur1.close()

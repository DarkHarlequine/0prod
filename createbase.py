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
    cur = konnekt.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS %s;" % \
               (defbase))
    cur.execute("GRANT ALL ON %s.* TO '%s'@'%s' IDENTIFIED BY '%s';" % \
               (defbase, defuser, defhost, defpasswd))
    cur.close()

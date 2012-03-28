import sys
import ConfigParser

class Connect(object):
    def __init__(self):
        config = ConfigParser.RawConfigParser()
        config.read('conf.cnf')
        self.mhost = config.get("MySQLopts", "host")
        self.user = config.get("MySQLopts", "user")
        self.passwd = config.get("MySQLopts", "passwd")
        self.base = config.get("MySQLopts", "base")
        self.rhost = config.get("Rabbitopts", "host")

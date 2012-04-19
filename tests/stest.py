import sys
import unittest
from mock import Mock
sys.path.append ("../0_prod/0_prod")
from server import Server



class ServerTest(unittest.TestCase):
    def setUp(self):
        self.tstobj = Mock(spec = Server)
        self.msg = "Test message"


    def testCut(self):
        incorrect_msg = "\n(LTest message,'ZY)"
        self.tstobj.cut(incorrect_msg)
        print self.tstobj.cut.mock_calls

    def testInsert(self):
        self.tstobj.insert(self.msg)
        print self.tstobj.insert.mock_calls


    def testLastIdRequest(self):
        self.tstobj.last_added_id_request()
        print self.tstobj.last_added_id_request.mock_calls


    def testTaskStatRequest(self):
        self.tstobj.task_stat_request(1)
        print self.tstobj.task_stat_request.mock_calls


if __name__ == '__main__':
   unittest.main()

import sys
import unittest
from mock import Mock
sys.path.append ("../0_prod")
import server



class ServerTest(unittest.TestCase):
    def setUp(self):
        self.msg = "Test message"
        self.mockCursor = Mock({'execute': Mock(), 'fetchall':Mock()})
        konnekt = Mock( { "cursor" : self.mockCursor, "__enter__": None, "__exit__": None } )


    def testCut(self):
        incorrect_msg = "\n(LTest message,'ZY)"
        correct_msg = server.cut(incorrect_msg)
        self.assertEqual(self.msg, correct_msg)


    def testInsert(self):
        server.insert(self.msg)
        self.konnekt.mock_calls


    def testLastIdRequest(self):
        server.last_added_id_request()
        self.konnekt.mock_calls


    def testTaskStatRequest(self):
        server.task_stat_request(1)
        self.konnekt.mock_calls


if __name__ == '__main__':
    #mockCursor = Mock({'execute': Mock(), 'fetchall':Mock()})
    #server.konnekt = Mock( { "cursor" : mockCursor, "__enter__": None, "__exit__": None } )
    unittest.main()

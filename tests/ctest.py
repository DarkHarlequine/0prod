import sys
sys.path.append ("../0_prod/0_prod")
import client
import unittest
from mock import Mock

class TestClient(unittest.TestCase):


    def setUp(self):
        self.tstobj = Mock(spec=client.Client)
        self.tstobj.connection = Mock(return_value = 'Mocked connection')
        self.tstobj.response = Mock(return_value = 'Mocked response')
        

 
    def testJob(self): 
        key = self.tstobj.job
        self.assertIsNotNone(key)


    def testMarker(self):
        key1 = client.marker(1)
        key2 = client.marker(2)
        self.assertEqual(key1, 'Z')
        self.assertEqual(key2, 'Y')


    def testCall(self):
        self.tstobj.call 
        print self.tstobj.call.mock_calls
 

if __name__=='__main__':
    unittest.main()

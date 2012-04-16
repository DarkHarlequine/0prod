import sys
sys.path.append ("../0_prod")
import client
import unittest


class TestClient(unittest.TestCase):


    def setUp(self):
        self.tstobj = client.Client
#       self.tstjob = {'Play game', 'Play guitar', 'Kill all humans', 'Conquer\
#                       this world', 'Drink a bottle'}
 
    def testJob(self): 
        key = self.tstobj.job
        self.assertIsNotNone(key)


    def testMarker(self):
        key1 = client.marker(1)
        key2 = client.marker(2)
        self.assertEqual(key1, 'Z')
        self.assertEqual(key2, 'Y')
if __name__=='__main__':
    unittest.main()

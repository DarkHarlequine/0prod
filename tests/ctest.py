import sys
sys.path.append ("../0_prod")
import client
import unittest


class TestClient(unittest.TestCase):


    def setUp(self):
        self.client = server.Client
        self.tstjob = {'Play game', 'Play guitar', 'Kill all humans', 'Conquer\
                       this world', 'Drink a bottle'}
 
    def testJob(self): 
        key = client.job()
        self.assertEqual(key, self.tstjob(1))


if __name__=='__main__':
    unittest.main()

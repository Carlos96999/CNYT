import unittest
import Clásico_a_cuántico

class TestMyModule(unittest.TestCase):

    def test_cani(self):
        self.assertEqual(Clásico_a_cuántico.Canicas([[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                                                     [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                                                     [(1,0),(0,0),(0,0),(0,0),(0,0),(1,0)],
                                                     [(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)],
                                                     [(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
                                                     [(1,0),(0,0),(0,0),(0,0),(1,0),(0,0)],
                                                     ], [(6,0),(2,0),(1,0),(5,0),(3,0),(10,0)],3), [(0,0),(0,0),(1,0),(5,0),(9,0),(16,0)])

    def test_prob(self):
        self.assertEqual(Clásico_a_cuántico.Probabilidad([[(0,0),(1/3,0),(2/3,0)],
                                                          [(1/6,0),(1/2,0),(1/3,0)],
                                                          [(5/6,0),(1/6,0),(0,0)]], [(1/3,0),(0,0),(2/3,0)]),[(4/9,0),(5/18,0),(5/18,0)])

    def testDob(self):
        self.assertEquals(Clásico_a_cuántico.DobleRendija([[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                                                           [(1/(2)**(1/2),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                                                           [(1/(2)**(1/2),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                                                           [(0,0),(-1/(6)**(1/2),1/(6)**(1/2)),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],
                                                           [(0,0),(-1/(6)**(1/2),-1/(6)**(1/2)),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
                                                           [(0,0),(1/(6)**(1/2),-1/(6)**(1/2)),(-1/(6)**(1/2),1/(6)**(1/2)),(0,0),(0,0),(1,0),(0,0),(0,0)],
                                                           [(0,0),(0,0),(-1/(6)**(1/2),-1/(6)**(1/2)),(0,0),(0,0),(0,0),(1,0),(0,0)],
                                                           [(0,0),(0,0),(1/(6)**(1/2),-1/(6)**(1/2)),(0,0),(0,0),(0,0),(0,0),(1,0)]]),
                          [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (-0.2886751345948129, 0.2886751345948129), (-0.2886751345948129, -0.2886751345948129), (0.0, 0.0), (-0.2886751345948129, -0.2886751345948129), (0.2886751345948129, -0.2886751345948129)])
                                                    
if __name__ == "__main__":
    unittest.main()

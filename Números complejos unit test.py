import unittest
import Librería_números_complejos

class TestMyModule(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(Librería_números_complejos.Suma([5,8],[3,7]),(8,15))
    def test_res(self):
        self.assertEqual(Librería_números_complejos.Resta([5,8],[3,7]),(2,1))
    def test_prod(self):
        self.assertEqual(Librería_números_complejos.Producto([5,8],[3,7]),(-41,59))
    def test_divi(self):
        self.assertEqual(Librería_números_complejos.Division([5,8],[3,7]),(1.2241379310344827,-0.1896551724137931))
    def test_mod(self):
        self.assertEqual(Librería_números_complejos.Modulo([5,8]),9.433981132056603)
    def test_conju(self):
        self.assertEqual(Librería_números_complejos.Conjugado([5,8]),(5,-8))
    def test_cp(self):
        self.assertEqual(Librería_números_complejos.ConverCartePola([5,8]),(9.433981132056603,57.9946167919165))
    def test_pc(self):
        self.assertEqual(Librería_números_complejos.ConverPolaCarte(78,69),(77.48444961833718,-8.953215475088603))
    def test_fas(self):
        self.assertEqual(Librería_números_complejos.Fase([5,8]),57.9946167919165)
    def test_SumVec(self):
        self.assertEqual(Librería_números_complejos.SumaVector([(5,8),(4,9)],[(3,7),(6,7)]),[(8,15),(10,16)])
    def test_InvVec(self):
        self.assertEqual(Librería_números_complejos.InversoVector([(5,8),(4,9)]),[(-5,-8),(-4,-9)])
    def test_ProdEscVec(self):
        self.assertEqual(Librería_números_complejos.ProductoEscalarVector((5,8),[(3,7),(1,-5)]),[(-41,59),(45,-17)])
    def test_SumMatr(self):
        self.assertEqual(Librería_números_complejos.SumaMatriz([[(3,5),(2,1)],[(14,-1),(16,0)]],[[(7,9),(6,-2)],[(1,-4),(5,3)]]),[[(10,14),(8,-1)],[(15,-5),(21,3)]])
    def test_InvMatr(self):
        self.assertEqual(Librería_números_complejos.InversaMatriz([[(3,5),(2,1)],[(14,-1),(16,0)]]),[[(-3,-5),(-2,-1)],[(-14,1),(-16,0)]])
    def test_ProdEscMatr(self):
        self.assertEqual(Librería_números_complejos.ProductoEscalarMatriz((6,0),[[(3,5),(2,1)],[(14,-1),(16,0)]]),[[(18,30),(12,6)],[(84,-6),(96,0)]])
    def test_MatrTrans(self):
        self.assertEqual(Librería_números_complejos.MatrizTranspuesta([[(4,7),(3,8),(45,87)],[(12,3),(56,69),(0,1)],[(1,2),(45,13),(900,657)]]),[[(4,7),(12,3),(1,2)],[(3,8),(56,69),(45,13)],[(45,87),(0,1),(900,657)]])
    def test_MatrConj(self):
        self.assertEqual(Librería_números_complejos.MatrizConjugada([[(1,2),(3,4),(5,-6)],[(7,-8),(2,-4),(9,3)],[(6,8),(7,-5),(2,6)]]),[[(1,-2),(3,-4),(5,6)],[(7,8),(2,4),(9,-3)],[(6,-8),(7,5),(2,-6)]])
    def test_MatrAdj(self):
        self.assertEqual(Librería_números_complejos.MatrizAdjunta([[(1,2),(2,-3),(3,4)],[(4,-5),(5,6),(6,-7)],[(7,8),(8,-9),(9,10)]]),[[(1,-2),(4,5),(7,-8)],[(2,3),(5,-6),(8,9)],[(3,-4),(6,7),(9,-10)]])
    def test_NormMatr(self):
        self.assertEqual(Librería_números_complejos.NormaMatriz([[(1,2),(2,-3),(3,4)],[(4,-5),(5,6),(6,-7)],[(7,8),(8,-9),(9,10)]]),25.865034312755125)
    def test_DistMatr(self):
        self.assertEqual(Librería_números_complejos.DistanciaMatriz([[(3,0),(7,0)],[(5,0),(8,0)]],[[(2,0),(9,0)],[(4,0),(-5,0)]]),13.228756555322953)
    #def test_ReviMatr(self):
    #    self.assertEqual(Librería_números_complejos.RevisarUnitaria([[
    
if __name__ == "__main__":
    unittest.main()

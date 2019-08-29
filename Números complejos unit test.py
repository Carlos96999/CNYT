import unittest
import Librería_números_complejos

class TestMyModule(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(Librería_números_complejos.Suma([5,8],[3,7]),[8,15])
    def test_res(self):
        self.assertEqual(Librería_números_complejos.Resta([5,8],[3,7]),[2,1])
    def test_prod(self):
        self.assertEqual(Librería_números_complejos.Producto([5,8],[3,7]),[-41,59])
    def test_divi(self):
        self.assertEqual(Librería_números_complejos.Division([5,8],[3,7]),[1.2241379310344827,-0.1896551724137931])
    def test_mod(self):
        self.assertEqual(Librería_números_complejos.Modulo([5,8]),9.433981132056603)
    def test_conju(self):
        self.assertEqual(Librería_números_complejos.Conjugado([5,8]),[5,-8])
    def test_cp(self):
        self.assertEqual(Librería_números_complejos.ConverCartePola([5,8]),[9.433981132056603,57.9946167919165])
    def test_pc(self):
        self.assertEqual(Librería_números_complejos.ConverPolaCarte(78,69),[77.48444961833718,-8.953215475088603])
    def test_fas(self):
        self.assertEqual(Librería_números_complejos.Fase([5,8]),57.9946167919165)
        
if __name__ == "__main__":
    unittest.main()

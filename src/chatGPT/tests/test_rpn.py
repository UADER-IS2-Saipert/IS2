import unittest
from rpn import evaluar, RPNError
import math

class TestRPN(unittest.TestCase):
    # ---------- Operaciones correctas ----------
    def test_suma(self): self.assertEqual(evaluar("5 3 +"), 8.0)
    def test_resta(self): self.assertEqual(evaluar("5 3 -"), 2.0)
    def test_multiplicacion(self): self.assertEqual(evaluar("5 3 *"), 15.0)
    def test_division(self): self.assertEqual(evaluar("10 2 /"), 5.0)
    def test_float(self): self.assertAlmostEqual(evaluar("5 2 /"),2.5)
    def test_negativos(self): self.assertEqual(evaluar("5 -3 *"), -15.0)
    def test_constantes(self):
        r=evaluar("p e +")
        self.assertTrue(r>5)
    def test_potencia(self): self.assertEqual(evaluar("2 3 yx"),8.0)
    def test_inverso(self): self.assertEqual(evaluar("4 1/x"),0.25)
    def test_chs(self): self.assertEqual(evaluar("5 chs"), -5.0)
    def test_trig(self): self.assertAlmostEqual(evaluar("90 sin"),1,places=5)
    def test_log(self): self.assertEqual(evaluar("100 log"),2.0)
    def test_ln(self): self.assertAlmostEqual(evaluar("1 ln"),0)
    def test_memoria(self): self.assertEqual(evaluar("5 STO 00 RCL 00"),5.0)
    def test_dup(self): self.assertEqual(evaluar("5 dup +"),10.0)
    def test_swap(self): self.assertEqual(evaluar("2 3 swap -"),1.0)
    def test_drop(self): self.assertEqual(evaluar("5 3 drop"),5.0)
    def test_clear(self): self.assertEqual(evaluar("5 3 clear 2"),2.0)

    # ---------- Tests de errores ----------
    def test_error_pila_vacia(self):
        with self.assertRaises(RPNError): evaluar("+")
    def test_error_division_cero(self):
        with self.assertRaises(RPNError): evaluar("5 0 /")
    def test_error_token(self):
        with self.assertRaises(RPNError): evaluar("5 x +")
    def test_error_memoria(self):
        with self.assertRaises(RPNError): evaluar("5 STO 10")
    def test_error_resultado(self):
        with self.assertRaises(RPNError): evaluar("5 3")
    def test_error_dominio(self):
        with self.assertRaises(RPNError): evaluar("-1 sqrt")
    def test_swap_error(self):
        with self.assertRaises(RPNError): evaluar("5 swap")
    def test_dup_error(self):
        with self.assertRaises(RPNError): evaluar("dup")
    def test_rcl_invalido(self):
        with self.assertRaises(RPNError): evaluar("RCL 10")
    def test_sto_sin_valor(self):
        with self.assertRaises(RPNError): evaluar("STO 00")
    def test_asin_borde(self): self.assertEqual(evaluar("1 asin"),90)
    def test_acos_borde(self): self.assertEqual(evaluar("1 acos"),0)
    def test_atan(self): self.assertAlmostEqual(evaluar("1 atan"),45,places=5)

if __name__=="__main__":
    unittest.main()
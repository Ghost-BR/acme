# coding: utf-8
import unittest

import acme


class AcmeTestCase(unittest.TestCase):

    def tearDown(self):
        acme.compressor = False

    def test_first_call(self):
        self.assertEqual(acme.compressor, False)
        temp, custo = acme.refrigera(30, 30)
        self.assertEqual(custo, 0.50)
        self.assertAlmostEqual(temp, 30, delta=2)
        self.assertEqual(acme.compressor, True)
        temp, custo = acme.refrigera(30, 30)
        self.assertEqual(custo, 0.0)
        self.assertAlmostEqual(temp, 30, delta=2)
        self.assertEqual(acme.compressor, True)

    def test_1_grau_acima(self):
        temp, custo = acme.refrigera(31, 30)
        self.assertEqual(custo, 0.50)
        self.assertAlmostEqual(temp, 30, delta=2)

    def test_2_grau_acima(self):
        temp, custo = acme.refrigera(32, 30)
        self.assertEqual(custo, 0.50)
        self.assertAlmostEqual(temp, 30, delta=2)

    def test_3_grau_acima(self):
        temp, custo = acme.refrigera(33, 30)
        self.assertAlmostEqual(custo, 0.60, delta=0.01)
        self.assertAlmostEqual(temp, 30, delta=2)

    def test_simulator_360min(self):
        custo = acme.simulador(30, 20, 0.5, 360)
        self.assertAlmostEqual(custo, 19.3, delta=0.01)


if __name__ == "__main__":
    unittest.main()

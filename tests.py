# coding: utf-8
import unittest

import acme


class AcmeTestCase(unittest.TestCase):

    def tearDown(self):
        acme.compressor = False

    def test_first_call(self):
        self.assertEqual(acme.compressor, False)
        custo = acme.refrigera(30, 30)
        self.assertEqual(custo, 0.50)
        self.assertEqual(acme.compressor, True)
        custo = acme.refrigera(30, 30)
        self.assertEqual(custo, 0.0)
        self.assertEqual(acme.compressor, True)

    def test_1_grau_acima(self):
        custo = acme.refrigera(31, 30)
        self.assertEqual(custo, 0.50)

    def test_2_grau_acima(self):
        custo = acme.refrigera(32, 30)
        self.assertEqual(custo, 0.50)

    def test_3_grau_acima(self):
        custo = acme.refrigera(33, 30)
        self.assertAlmostEqual(custo, 1.00, delta=0.01)

    def test_over_time(self):
        custo = acme.refrigera(30, 20)
        self.assertAlmostEqual(custo, 1.70, delta=0.01)
        # passou 2 min desde ligado
        custo = acme.refrigera(21, 20)
        self.assertAlmostEqual(custo, 0.0, delta=0.01)
        # passou 5 min desde ligado
        custo = acme.refrigera(22.5, 20)
        self.assertAlmostEqual(custo, 0.50, delta=0.01)

if __name__ == "__main__":
    unittest.main()

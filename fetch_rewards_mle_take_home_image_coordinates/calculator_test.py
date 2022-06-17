import unittest
import calculator
import math

class Test_calculator_test(unittest.TestCase):
    def test_1(self):
        result1 = (0.0, 3.0, 0.0, 3.0)

        result2 = calculator.min_max_xy([(0, 0), (3, 0), (0, 3), (3, 3)])

        for i in range(len(result1)):
            self.assertTrue(math.isclose(result1[i], result2[i]), "val1: {0}; val2: {1}".format(result1[i], result2[i]))

    def test_2(self):
        result1 = (0.0, 3.0, 0.0, 3.0)

        result2 = calculator.min_max_xy([(3, 0), (0, 3), (3, 3), (0, 0)])

        for i in range(len(result1)):
            self.assertTrue(math.isclose(result1[i], result2[i]))

    def test_3(self):
        result = [[(1.0, 1.0), (2.0, 1.0), (3.0, 1.0)],
                  [(1.0, 2.0), (2.0, 2.0), (3.0, 2.0)],
                  [(1.0, 3.0), (2.0, 3.0), (3.0, 3.0)]]

        self.assertListEqual(result, calculator.generate_points(1.0, 3.0, 1.0, 3.0, 3, 3))

    def test_4(self):
        result = [[(0.0, 0.0), (0.5, 0.0), (1.0, 0.0), (1.5, 0.0), (2.0, 0.0), (2.5, 0.0), (3.0, 0.0)],
                  [(0.0, 0.5), (0.5, 0.5), (1.0, 0.5), (1.5, 0.5), (2.0, 0.5), (2.5, 0.5), (3.0, 0.5)],
                  [(0.0, 1.0), (0.5, 1.0), (1.0, 1.0), (1.5, 1.0), (2.0, 1.0), (2.5, 1.0), (3.0, 1.0)],
                  [(0.0, 1.5), (0.5, 1.5), (1.0, 1.5), (1.5, 1.5), (2.0, 1.5), (2.5, 1.5), (3.0, 1.5)],
                  [(0.0, 2.0), (0.5, 2.0), (1.0, 2.0), (1.5, 2.0), (2.0, 2.0), (2.5, 2.0), (3.0, 2.0)]]

        self.assertListEqual(result, calculator.generate_points(0.0, 3.0, 0.0, 2.0, 7, 5))

    def test_5(self):
        result1 = [[(0.0, 0.0),  (0.333, 0.0),   (0.666, 0.0),   (1.0, 0.0),   (1.333, 0.0),   (1.666, 0.0),   (2.0, 0.0)], 
                  [(0.0, 0.333), (0.333, 0.333), (0.666, 0.333), (1.0, 0.333), (1.333, 0.333), (1.666, 0.333), (2.0, 0.333)], 
                  [(0.0, 0.666), (0.333, 0.666), (0.666, 0.666), (1.0, 0.666), (1.333, 0.666), (1.666, 0.666), (2.0, 0.666)], 
                  [(0.0, 1.0),   (0.333, 1.0),   (0.666, 1.0),   (1.0, 1.0),   (1.333, 1.0),   (1.666, 1.0),   (2.0, 1.0)], 
                  [(0.0, 1.333), (0.333, 1.333), (0.666, 1.333), (1.0, 1.333), (1.333, 1.333), (1.666, 1.333), (2.0, 1.333)],
                  [(0.0, 1.666), (0.333, 1.666), (0.666, 1.666), (1.0, 1.666), (1.333, 1.666), (1.666, 1.666), (2.0, 1.666)],
                  [(0.0, 2.0),   (0.333, 2.0),   (0.666, 2.0),   (1.0, 2.0),   (1.333, 2.0),   (1.666, 2.0),   (2.0, 2.0)]]

        result2 = calculator.generate_points(0.0, 2.0, 0.0, 2.0, 7, 7)

        for i in range(len(result1)):
            for j in range(len(result1[i])):
                self.assertTrue(math.isclose(result1[i][j][0], result2[i][j][0], abs_tol=0.01))
                self.assertTrue(math.isclose(result1[i][j][1], result2[i][j][1], abs_tol=0.01))

if __name__ == '__main__':
    unittest.main()

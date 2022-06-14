import unittest
import calculator

class Test_calculator_test(unittest.TestCase):
    def test_1(self):
        result = [[(1.0, 1.0), (2.0, 1.0), (3.0, 1.0)],
                  [(1.0, 2.0), (2.0, 2.0), (3.0, 2.0)],
                  [(1.0, 3.0), (2.0, 3.0), (3.0, 3.0)]]

        self.assertListEqual(result, calculator.generate_points(1.0, 3.0, 1.0, 3.0, 3, 3))

if __name__ == '__main__':
    unittest.main()

import unittest
from ..domaci_sv_57_2023 import calculate_postfix, infix_to_postfix
from ..errors import *

class TestCalculatePostfix(unittest.TestCase):

    def test_calculate_postfix_1(self):
        input_expression = "6.11 - 74 * 2 "
        excepted_output = -141.89
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_postfix_2(self):
        input_expression = "(24 - 7) ^ (3.2 - 2)"
        excepted_output = 29.9597859131
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_postfix_3(self):
        input_expression = "20 * 7.9 / (3 - 7)"
        excepted_output = -39.5
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_postfix_4(self):
        input_expression = "-20 * .9 / (3 - 7)"
        excepted_output = 4.5
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_postfix_5(self):
        input_expression = "2*3+4^(5-1-(-10+2*3*2))"
        excepted_output = 22
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_postfix_6(self):
        input_expression = "2 + 3 * 4 - (5 / 6) ^ 2"
        excepted_output = 13.3055555555555
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_postfix_7(self):
        input_expression = "(-2 + 3) * (4.36 - (-5)) / (-6) ^ 2"
        excepted_output = 0.26
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_postfix_8(self):
        input_expression = "-2^3^4^5-5*5/25+1"
        excepted_output = -1.152921504606847e+18
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_postfix_9(self):
        input_expression = "-(-(-5.25-6))^5*(-4.99)-2"
        excepted_output = 899212.2028808594
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)
    
    def test_calculate_postfix_10(self):
        input_expression = "-(-(-(-(-(-(-(-(-(-5.55-(-5.55))^2)^3)^4)^5)^6)^7)^8)^9)^10"
        excepted_output = 0
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_postfix_11(self):
        input_expression = "-2^2"
        excepted_output = -4
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_postfix_12(self):
        input_expression = "2^0"
        excepted_output = 1
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    ############     INVALID     ############

    def test_calculate_postfix_13(self):
        input_expression = "10/0"
        self.assertRaises(DivisionByzeroError, calculate_postfix, infix_to_postfix(input_expression))

    def test_calculate_postfix_14(self):
        input_expression = "15/(2-2)"
        self.assertRaises(DivisionByzeroError, calculate_postfix, infix_to_postfix(input_expression))

    def test_calculate_postfix_15(self):
        input_expression = "12 / (3 - 9/3) "
        self.assertRaises(DivisionByzeroError, calculate_postfix, infix_to_postfix(input_expression))

    def test_calculate_postfix_16(self):
        input_expression = "(-2)^0.5"
        self.assertRaises(ComplexRootError, calculate_postfix, infix_to_postfix(input_expression))

    def test_calculate_postfix_17(self):
        input_expression = "(5-5^2)^(1/3)"
        self.assertRaises(ComplexRootError, calculate_postfix, infix_to_postfix(input_expression))

    def test_calculate_postfix_18(self):
        input_expression = "0/0"
        self.assertRaises(UndefinedOperationError, calculate_postfix, infix_to_postfix(input_expression))

    
    def test_calculate_postfix_19(self):
        input_expression = "-(-2+2)/(5-5)"
        self.assertRaises(UndefinedOperationError, calculate_postfix, infix_to_postfix(input_expression))
    
    def test_calculate_postfix_20(self):
        input_expression = "0*0^(-1)"
        self.assertRaises(DivisionByzeroError, calculate_postfix, infix_to_postfix(input_expression))

if __name__ == '__main__':
    unittest.main()
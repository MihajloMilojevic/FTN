import unittest
from ..domaci_sv_57_2023 import infix_to_postfix
from ..errors import *

class TestInfixToPostfix(unittest.TestCase):
    ############     VALID     ############
    def test_infix_to_postfix_1(self):
        input_expression = "6.11 - 74 * 2 "
        excepted_output = "6.11 74 2 * -"
        function_output = infix_to_postfix(input_expression)
        output_string = " ".join([str(elem) for elem in function_output])
        self.assertEqual(output_string, excepted_output)


    def test_infix_to_postfix_2(self):
        input_expression = "(24 - 7) ^ (3.2 + (-7))"
        excepted_output = "24 7 - 3.2 -7 + ^"
        function_output = infix_to_postfix(input_expression)
        output_string = " ".join([str(elem) for elem in function_output])
        self.assertEqual(output_string, excepted_output)


    def test_infix_to_postfix_3(self):
        input_expression = "-20 * 7.9 / (3 - 7)"
        excepted_output = "-20 7.9 * 3 7 - /"
        function_output = infix_to_postfix(input_expression)
        output_string = " ".join([str(elem) for elem in function_output])
        self.assertEqual(output_string, excepted_output)


    def test_infix_to_postfix_4(self):
        input_expression = "-20 * .9 / (3 - 7)"
        excepted_output = "-20 0.9 * 3 7 - /"
        function_output = infix_to_postfix(input_expression)
        output_string = " ".join([str(elem) for elem in function_output])
        self.assertEqual(output_string, excepted_output)


    def test_infix_to_postfix_5(self):
        input_expression = "2*3+4^(5-1-(-10+2*3*2))"
        excepted_output = "2 3 * 4 5 1 - -10 2 3 * 2 * + - ^ +"
        function_output = infix_to_postfix(input_expression)
        output_string = " ".join([str(elem) for elem in function_output])
        self.assertEqual(output_string, excepted_output)


    def test_infix_to_postfix_6(self):
        input_expression = "2 + 3 * 4 - (5 / 6) ^ 2"
        excepted_output = "2 3 4 * + 5 6 / 2 ^ -"
        function_output = infix_to_postfix(input_expression)
        output_string = " ".join([str(elem) for elem in function_output])
        self.assertEqual(output_string, excepted_output)


    def test_infix_to_postfix_7(self):
        input_expression = "(-2 + 3) * (4.36 - (-5)) / (-6) ^ 2"
        excepted_output = "-2 3 + 4.36 -5 - * -6 2 ^ /"
        function_output = infix_to_postfix(input_expression)
        output_string = " ".join([str(elem) for elem in function_output])
        self.assertEqual(output_string, excepted_output)


    def test_infix_to_postfix_8(self):
        input_expression = "-2^3^4^5-5*5/25+1"
        excepted_output = "2 3 ^ 4 ^ 5 ^ ~ 5 5 * 25 / - 1 +"
        function_output = infix_to_postfix(input_expression)
        output_string = " ".join([str(elem) for elem in function_output])
        self.assertEqual(output_string, excepted_output)


    def test_infix_to_postfix_9(self):
        input_expression = "-(-(-5.25-6))^5*(-4.99)-2"
        excepted_output = "-5.25 6 - ~ 5 ^ ~ -4.99 * 2 -"
        function_output = infix_to_postfix(input_expression)
        output_string = " ".join([str(elem) for elem in function_output])
        self.assertEqual(output_string, excepted_output)


    def test_infix_to_postfix_10(self):
        input_expression = "-(-(-(-(-(-(-(-(-(-5.55-(-5.55))^2)^3)^4)^5)^6)^7)^8)^9)^10"
        excepted_output = "-5.55 -5.55 - 2 ^ ~ 3 ^ ~ 4 ^ ~ 5 ^ ~ 6 ^ ~ 7 ^ ~ 8 ^ ~ 9 ^ ~ 10 ^ ~"
        function_output = infix_to_postfix(input_expression)
        output_string = " ".join([str(elem) for elem in function_output])
        self.assertEqual(output_string, excepted_output)

    ############     INVALID     ############

    def test_infix_to_postfix_11(self):
        input_expression = ""
        self.assertRaises(EmptyExpressionError, infix_to_postfix, input_expression)


    def test_infix_to_postfix_12(self):
        input_expression = "2+()"
        self.assertRaises(EmptyParenthesisError, infix_to_postfix, input_expression)


    def test_infix_to_postfix_13(self):
        input_expression = "-2-"
        self.assertRaises(InvalidOperatorOrderError, infix_to_postfix, input_expression)


    def test_infix_to_postfix_14(self):
        input_expression = "2^-3"
        self.assertRaises(InvalidOperatorOrderError, infix_to_postfix, input_expression)


    def test_infix_to_postfix_15(self):
        input_expression = "2+"
        self.assertRaises(InvalidOperatorOrderError, infix_to_postfix, input_expression)

        
    def test_infix_to_postfix_16(self):
        input_expression = "+5-3"
        self.assertRaises(InvalidOperatorOrderError, infix_to_postfix, input_expression)


    def test_infix_to_postfix_17(self):
        input_expression = "((2+3)"
        self.assertRaises(NoCloseParenthesisError, infix_to_postfix, input_expression)


    def test_infix_to_postfix_18(self):
        input_expression = "(2+3))"
        self.assertRaises(NoOpenParenthesisError, infix_to_postfix, input_expression)


    def test_infix_to_postfix_19(self):
        input_expression = "2a+3b"
        self.assertRaises(UnknownCharacterError, infix_to_postfix, input_expression)


    def test_infix_to_postfix_20(self):
        input_expression = "-(-(-(-(-(-(-(-(-(-5.55-(-5.55))^2)^3)^4)^5)^6)^7)^8)^9)^10^"
        self.assertRaises(InvalidOperatorOrderError, infix_to_postfix, input_expression)

if __name__ == '__main__':
    unittest.main()
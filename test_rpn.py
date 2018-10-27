import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2,result)
	def test_sub(self):
		result = rpn.calculate('4 3 -')
		self.assertEqual(1,result)
	def test_multiple(self):
		result=rpn.calculate('2 5 *')
		self.assertEqual(10,result)
	def test_division(self):
		result=rpn.calculate('12 4 /')
		self.assertEqual(3,result)
	def test_carat(self):
		result= rpn.calculate('2 5 ^')
		self.assertEqual(32,result)

import unittest
from projetAventure import TextAdventure

class TestTextAdventure(unittest.TestCase):
	
	def setUp(self):
		self.t = TextAdventure('text.sample.json', 'Intro')

	def test_get_global_var(self):
		valid_test = {
			"clef": False,
			"mecanisme": False
		}
		self.t.get_global_var()
		
		self.assertEqual(
			self.t.global_var,
			valid_test
		)

	def test_handle_define(self):
		'''Check if hello is in global variables and if it's equal to true'''
		self.t.handle_define('hello', 0)

		key = "hello"
		value = True

		self.assertIn(key, self.t.global_var)
		self.assertEqual(self.t.global_var[key], value)


		



		






if __name__ == '__main__':
	unittest.main()


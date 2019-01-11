import unittest
from projetAventure import TextAdventure

class TestTextAdventure(unittest.TestCase):
	
	def setUp(self):
		self.t = TextAdventure('text.sample.json', 'Intro')

	def test_get_global_var(self):
		'''Check if global value are loaded'''
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

	def test_next_choice_next(self):
		'''Check if the choice selection is correct with simple simple branchement'''
		self.assertEqual(self.t.next_choice('hello', 0), 'hello2')

	def test_next_choice_require_true(self):
		'''Check if the choice selection is correct with require branchement (true)'''
		self.t.global_var['a'] = True
		self.assertEqual(self.t.next_choice('hello2', 0), 'hello3')

	def test_next_choice_require_false(self):
		'''Check if the choice selection is correct with require branchement (false)'''
		self.t.global_var['a'] = False
		self.assertEqual(self.t.next_choice('hello2', 0), 'hello4')


    # def next_choice(self, name: str, n: int) -> str:
    #     choice = self.ppt['choix'][name][n]
    #     if 'require' in choice:
    #         if self.global_var[choice["require"]["name"]]:
    #             return choice["require"]["true"]
    #         else:
    #             return choice["require"]["false"]

    #     else:
    #         return choice['next']



		






if __name__ == '__main__':
	unittest.main()


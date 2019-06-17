import unittest
from Sample import core

class TestCore(unittest.TestCase):
	def test_hello_world(self):
		program = core.Core()
		self.assertEqual(program.hello_world(), "Hello World!")
import unittest
from app.classes.books import Book

class TestBook(unittest.TestCase):
	"""
	This uncludes the tests for the books model
	"""

	def setUp(self):
		self.book = Book('User')


if __name__ == '__main__':
	unittest.main()
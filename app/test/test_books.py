import unittest
from app.classes.books import Book

class TestBook(unittest.TestCase):
	"""
	This uncludes the tests for the books model
	"""

	def setUp(self):
		self.books = Book('User')

	def test_borrow_book(self):
		"""
		Test to borrow a book
		"""
		self.books.borrow_book('book1')
		self.assertEqual(self.user.books, ['book1'])


if __name__ == '__main__':
	unittest.main()
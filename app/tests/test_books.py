import unittest
from app.classes.books import Books

class TestBook(unittest.TestCase):
	"""
	This uncludes the tests for the books model
	"""

	def setUp(self):
		self.book = Book('User')

	def test_borrow_book(self):
		"""
		Test to borrow a book
		"""
		self.user.borrow_book('book1')
		self.assertEqual(self.user.books, ['book1'])



	def test_return_book(self):
		"""
		Test to return a book
		"""
		self.user.books.append('book1')
		self.user.books.append('book3')
		self.user.return_book('book3')
		self.assertEqual(self.user.books, ['book1'])

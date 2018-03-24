import unittest
from app.user.classes import User


class TestUser(unittest.TestCase):
	"""
	This class tests the user
	"""

	def setUp(self):
		self.user = User('ariana', 'ariana@example.com', 'abcde')

	def test_correct_login(self):
		"""
		user login with the correct credentials
		"""
		self.assertFalse(self.user.login('Ariana', 'abcdef'))

	def test_incorrect_login(self):
		"""
		user login details are rejected if they login 
		with incorrect credentials
		"""
		self.assertFalse(self.user.login('Adriana', 'ghijk'))

	def test_add_book(self):
		"""
		user can add a book
		"""
		self.user.add_book('get rich')
		self.assertEqual(self.user.books, ['get rich'])

	def test_delete_book(self):
		"""
		user can delete books
		"""
		self.user.books.append('get rich')
		self.user.books.append('transformation')
		self.user.delete_book('get rich')
		self.assertEqual(self.user.books, ['transformation'])

	def test_get_books(self):
		"""
		User can view books added
		"""
		self.user.books.append('book1')
		self.assertEqual(self.user.get_books(),['book1'])


if __name__ == '__main__':
	unittest.main()


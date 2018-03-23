class Book(object):
	"""
	class modelling the Book
	"""

	def __init__(self, name):
		self.name = name

	def borrow_book(self, book):
		"""
		function to borrow books
		"""
		self.books.append(book)

	def return_book(self, book):
		"""
		function to return books
		"""
		
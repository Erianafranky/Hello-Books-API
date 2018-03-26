class Book(object):
	"""
	class modelling the Book
	"""

	def __init__(self, name):
		self.name = name
		self.books = []

	def borrow_book(self, book):
		"""
		function to borrow books
		"""
		self.books.append(book)

	
		
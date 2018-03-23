class User(object):
	"""
	class to model the user
	"""
	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password
		self.books = []

	def login(self, username, password):
		"""
		function to handle ability of user to login
		"""
		if username == self.username and password == self.password:
			return True
		else:
			return False

	def add_book(self, book):
		"""function to add books
		"""
		self.books.append(book)

	def delete_book(self, book):
		"""
		function to delete books
		"""
		self.books.remove(book)

	def get_book(self):
		"""
		function to get all the books created
		"""
		return self.books

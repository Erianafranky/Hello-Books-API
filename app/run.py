from flask import Flask, jsonify, request, abort, make_response, session
from classes.books import Book
from classes.user import User


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

users = {}
books = [{'id': 1, 'title' : 'get rich'},
         {'id': 2, 'title' : 'good deeds'},
         {'id': 3, 'title' : 'transformation'}] 

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error' : 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
	return make_response(jsonify({'error' : 'Bad request'}), 400)

@app.route('/api/v1/auth/register', methods=['POST'])
def create_account(username=None, email=None, password=None):
	"""
	function to register a user
	"""
	if request.method == 'POST':
		username = request.json['username']
		email = request.json['email']
		password = request.json['password']
		confirm_password = request.json['confirm']
		if password == confirm_password:
			user = User(username, email, password)
			users[user.username] = user
			return jsonify({'message' : 'You are successfully registered'})
		else:
			return jsonify({'message' : 'Passwords do not match'})

@app.route('/api/v1/auth/login', methods=['POST'])
def login(username=None, password=None):
	"""function to enable users to login
	"""
	if request.method == 'POST':
		data = request.get_json()
		username = data['username']
		password = data['password']

		user=users.get(username, False)
		if user and user.login(username, password):
			session['username'] = username
			session['logged_in'] = True
			return jsonify({'message' : 'You are logged in successfully'})
		else:
			abort(404)

@app.route('/api/v1/books', methods=['POST'])
def add_book():
	"""
	Function to create a book
	"""
	if not request.json or not 'title' in request.json:
		abort(400)
	book = {
	     'id' : books[-1]['id'] + 1,
	     'title' : request.json['title']
	}
	books.append(book)
	return jsonify({'book' : book}), 201	

@app.route('/api/v1/books/<bookId>', methods=['PUT'])
def update_book(bookId):
	"""
	Edits a single book using the id number
	"""
	book = [book for book in books if book['id'] == int(bookId)]
	if len(book) == 0:
		abort(404)
	if 'title' in request.json and type(request.json['title']) != str:
		abort(400)
	book[0]['title'] = request.json.get('title', book[0]['title'])
	return jsonify({'book' : book[0]})

@app.route('/api/v1/books', methods=['GET'])
def get_all_books():
	"""
	Returns the list of all created books
	"""
	return jsonify({'books' : books})

@app.route('/api/v1/books/<bookId>', methods=['GET'])
def get_book(bookId):
	"""Function to return one book using the id number
	"""
	book1 = [book1 for book1 in books if book1['id'] == int(bookId)]
	if len(book1) == 0:
		abort(404)
	return jsonify({'book1' : book1[0]})

@app.route('/api/v1/books/<bookId>', methods=['DELETE'])
def delete_book(bookId):
	"""Function to delete a book using the id number
	"""
	book = [book for book in books if book['id'] == int(bookId)]
	if len(book) == 0:
		abort(404)
	books.remove(book[0])
	return jsonify({'message' : 'Book deleted'})

@app.route('/api/v1/users/books/<bookId>', methods=['POST'])
def borrow_book(bookId):
	"""
	function to enable users to login
	"""
	book = [book for book in books if book['id'] == int(bookId)]
	if len(book) == 0:
		abort(404)

	books.remove(book[0])
	return jsonify({'message' : 'Book borrowed'})

@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
	"""
	Enables users to login
	"""
	session.clear()
	return jsonify({'message' : 'Successfully logged out'})

if __name__ == '__main__':
	app.run(debug = True)
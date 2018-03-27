from flask import Flask, jsonify, request, abort, make_response
from classes.books import Book
from classes.user import User


app = Flask(__name__)

books = [{'id': 1, 'name' : 'get rich'},
         {'id': 2, 'name' : 'good deeds'},
         {'id': 3, 'name' : 'transformation'}] 

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error' : 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
	return make_response(jsonify({'error' : 'Bad request'}), 400)



@app.route('/api/v1/books', methods=['POST'])
def add_book():
	"""
	Function to create a book
	"""
	if not request.json or 'name' not in request.json:
		abort(400)

	data = request.get_json()
	book = {
		 'id' : books[-1]['id'] + 1, 
		 'name' : data['name']
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
	if not request.json:
		abort(400)
	if 'name' in request.json and type(request.json['name']) != unicode:
		abort(400)
	book[0]['name'] = request.json.get('name', book[0]['name'])
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



@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
	return ""

if __name__ == '__main__':
	app.run(debug = True)
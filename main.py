from flask import Flask, request, jsonify
app = Flask(__name__)
from database import cursor, connection
from dotenv import load_dotenv
load_dotenv()


@app.route("/books", methods=["GET"])
def book_index():
    sql = "SELECT * FROM books;"
    cursor.execute(sql)
    books = cursor.fetchall()
    return jsonify(books)

@app.route("/books", methods=["POST"])
def book_create():
    sql = "INSERT INTO books (title) VALUES (%s);"
    cursor.execute(sql, (request.json["title"],))
    connection.commit()

    sql = "SELECT * FROM books ORDER BY ID DESC LIMIT 1"
    cursor.execute(sql)
    book = cursor.fetchone()
    return jsonify(book)

@app.route("/books/<int:id>", methods=["GET"])
def book_show(id):
    sql = "SELECT * FROM books WHERE id = %s;"
    cursor.execute(sql, (id,))
    book = cursor.fetchone()
    return jsonify(book)

@app.route("/books/<int:id>", methods=["PUT", "PATCH"])
def book_update(id):
    sql = "UPDATE books SET title = %s WHERE id = %s;"
    cursor.execute(sql, (request.json["title"], id))
    connection.commit()

    sql = "SELECT * FROM books WHERE id = %s"
    cursor.execute(sql, (id,))
    book = cursor.fetchone()
    return jsonify(book)

@app.route("/books/<int:id>", methods=["DELETE"])
def book_delete(id):
    sql = "SELECT * FROM books WHERE id = %s;"
    cursor.execute(sql, (id,))
    book = cursor.fetchone()
    
    if book:
        sql = "DELETE FROM books WHERE id = %s;"
        cursor.execute(sql, (id,))
        connection.commit()

    return jsonify(book)

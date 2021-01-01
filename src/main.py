from flask import Flask, request, jsonify, abort
app = Flask(__name__)
import psycopg2

connection = psycopg2.connect(
    database="spotify",
    user="postgres",
    password="postgres",
    host="54.206.181.154"
)

cursor = connection.cursor()

cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);")
connection.commit()

@app.route("/artists", methods=["GET"])
def book_index():
    #Return all books
    sql = "SELECT * FROM artists"
    cursor.execute(sql)
    artists = cursor.fetchall()
    return jsonify(artists)
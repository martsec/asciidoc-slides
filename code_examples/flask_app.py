from flask import Flask
import sqlite3

DB_FILE = "my_app.db"

app = Flask(__name__)

@app.route("/")
def main_page():
    return "<p>Hello, World!</p>"
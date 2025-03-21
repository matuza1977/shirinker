from flask import Flask, render_template, request, jsonify, redirect
import sqlite3
import string
import random

app = Flask(__name__)

# Criação do banco de dados
DATABASE = "database.db"


def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_url TEXT NOT NULL
            )
        """)


init_db()


def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('original_url')

    if not original_url:
        return jsonify({"message": "URL original é necessária"}), 400

    short_url = generate_short_url()

    # Salva no banco de dados
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO urls (original_url, short_url) VALUES (?, ?)", (original_url, short_url))
        conn.commit()

    return jsonify({"short_url": request.host_url + short_url})


@app.route('/<short_url>')
def redirect_url(short_url):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT original_url FROM urls WHERE short_url = ?", (short_url,))
        result = cursor.fetchone()

    if result:
        return redirect(result[0])
    else:
        return "<h1>URL não encontrada</h1>", 404


if __name__ == '__main__':
    app.run(debug=True)
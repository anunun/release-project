from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect("films.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM films ORDER BY \"Рік випуску\" DESC")
    films = cursor.fetchall()
    conn.close()
    return render_template('index.html', films=films)

@app.route('/film/<int:film_id>')
def show_film(film_id):
    conn = sqlite3.connect("films.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM films WHERE ID = ?", (film_id,))
    film = cursor.fetchone()
    conn.close()
    if film is None:
        return "Фільм не знайдено", 404
    return render_template("film.html", film=film)

@app.route("/index.html")
def film_page_2():
    return render_template("index.html")


app.run(debug=True)

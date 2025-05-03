from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    genre = request.args.get('genre')
    ftype = request.args.get('type')
    year = request.args.get('year')
    duration = request.args.get('duration')
    rating_min = request.args.get('rating_min')
    views_max = request.args.get('views_max')

    conn = sqlite3.connect("films.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = "SELECT * FROM films WHERE 1=1"
    params = []

    if genre:
        query += ' AND "Жанр" = ?'
        params.append(genre)

    if ftype:
        query += ' AND "Тип" = ?'
        params.append(ftype)

    if year:
        query += ' AND "Рік випуску" >= ?'
        params.append(year)

    if duration:
        query += ' AND "Тривалість (хв)" <= ?'
        params.append(duration)

    if rating_min:
        query += ' AND "Середня оцінка користувачів" >= ?'
        params.append(rating_min)

    if views_max:
        query += ' AND "Кількість переглядів" >= ?'
        params.append(views_max)

    print("QUERY:", query)
    print("PARAMS:", params)

    cursor.execute(query, params)
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
    return render_template("film.html", film=film)

@app.route("/index.html")
def film_page_2():
    return render_template("index.html")


app.run(debug=True)

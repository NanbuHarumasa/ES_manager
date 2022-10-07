from esManage import app
from flask import render_template, request, redirect, url_for
import sqlite3
DATABASE = "database.db"


@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    db_books = con.execute("SELECT * FROM books").fetchall()
    con.close()
    
    books = []
    for row in db_books:
        books.append({"title" : row[0], "price": row[1], "arrival_day":row[2]})
    
    """
    books = [{"title": "hugryWarm",
            "price": 1100,
            "arrival_day": "2020/7/12"},
            {"title": "guri",
            "price": 600,
            "arrival_day": "2020/7/13"}
    ]
    books = []
    """
            
    return render_template(
        "index.html",
        books=books
    )
    
@app.route("/form")
def form():
    return render_template(
        "form.html"
    )
    
@app.route("/register", methods=["POST"])
def register():
    title = request.form["title"]
    price = request.form["price"]
    arrival_day = request.form["arrival_day"]
    
    con = sqlite3.connect(DATABASE)
    con.execute("INSERT INTO books VALUES(?,?,?)", 
                [title, price, arrival_day])
    con.commit()
    con.close()
    return redirect(url_for("index"))
    


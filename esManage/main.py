from esManage import app
from flask import render_template, request, redirect, url_for
import sqlite3
DATABASE = "database.db"


@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    db_books = con.execute("SELECT * FROM es_record").fetchall()
    con.close()
    
    entry_sheet = []

    for row in db_books:
        entry_sheet.append({"company" : row[0], "problem": row[1], "theme":row[2]})


    return render_template(
        "index.html",
        entry_sheet = entry_sheet
    )
    
@app.route("/form")
def form():
    return render_template(
        "form.html"
    )
    
@app.route("/register", methods=["POST"])
def register():
    company = request.form["company"]
    problem = request.form["problem"]
    theme = request.form["theme"]
    
    con = sqlite3.connect(DATABASE)
    con.execute("INSERT INTO es_record VALUES(?,?,?)", 
                [company, problem, theme])
    con.commit()
    con.close()
    return redirect(url_for("index"))
    


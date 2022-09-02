
from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql

app = Flask(__name__)


@app.route("/")
def home():
    conn = sql.connect('crud.db')
    conn.row_factory=sql.Row
    cur = conn.cursor()
    cur.execute("select * from student")
    data = cur.fetchall()
    return render_template("index.html", datas = data)


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        s_name = request.form["name"]
        s_age = request.form["age"]
        s_language = request.form["language"]
        s_preference = request.form["preference"]
        conn=sql.connect("crud.db") #doubt
        cur=conn.cursor() #doubt
        cur.execute("insert into student (NAME,AGE,LANGUAGE,PREFERENCE) values(?,?,?,?)",(s_name,s_age,s_language,s_preference)) #why capital is used,why insert.
        conn.commit()
        return redirect(url_for('home'))

    return render_template("add_user.html") #what happen when we change the order of code.


@app.route("/edit_user/<string:id>",methods=["GET","POST"])
def edit_user(id):
    if request.method == "POST":
        pass
        s_name = request.form["name"]
        s_age = request.form["age"]
        s_language = request.form["language"]
        s_preference = request.form["preference"]
        conn=sql.connect("crud.db") 
        cur=conn.cursor() 
        cur.execute("update student set NAME=?, Age=?,LANGUAGE=?,PREFERENCE=? where ID=?",(s_name,s_age,s_language,s_preference,id))
        conn.commit()
        return redirect(url_for('home'))
    conn= sql.connect('crud.db')
    conn.row_factory= sql.Row
    cur=conn.cursor()
    cur.execute("select * from student where ID=?",(id,))
    data = cur.fetchone()
    return render_template("edit_user.html",datas=data)

@app.route("/delete_user/<string:id>",methods=["GET"])
def delete_user(id):
    conn = sql.connect("crud.db")
    cur = conn.cursor()
    cur.execute("delete from student where ID=?",(id,))
    conn.commit()
    return redirect(url_for('home'))


if __name__=="__main__":
    app.run(debug=True)

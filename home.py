from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(host='localhost',
                             database='buses',
                             user='root',
                             password='Emera1d0')

cursor = db.cursor()
cursor.execute("select description from busstop order by description;")

results = cursor.fetchall()

db1 = mysql.connector.connect(host='localhost',
                              database='course',
                              user='root',
                              password='Emera1d0'
                              )


def get_items(db1):
    cursor1 = db1.cursor()
    cursor1.execute("select * from students "
                    "order by students.lastName, "
                    "students.firstName")
    results1 = cursor1.fetchall()
    return results1


results1 = get_items(db1)


cursor2 = db1.cursor()
cursor2.execute("select moduleName from modules order by moduleName")

results3 = cursor2.fetchall()


@app.route('/')
def home():
    return render_template("homepage.html")


@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        student = request.form['student']
        cursor.execute('insert into students (firstName, lastName)'
                       'values (%, %)', student)
        db1.commit()
        return redirect('http://localhost:5000/insert', code=302)
    return render_template("insert.html", results1=results1)


@app.route('/test')
def test():
    return render_template("test.html", results=results)


@app.route('/course')
def course():
    return render_template("course.html", results1=results1)


@app.route('/modules')
def modules():
    return render_template("modules.html", results3=results3)


if __name__=="__main__":
    app.run()
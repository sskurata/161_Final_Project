from flask import Flask, render_template
from data import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/directory')
def directory():
    return render_template('directory.html')

@app.route('/house/<house>')
def house(house):
    student_list = read_student_by_house(house)
    return render_template("house.html", house=house, students=student_list)

@app.route('/house/<int:student_id>')
def student(student_id):
    student = read_student_by_student_id(student_id)
    return render_template("student.html",student=student)

if __name__ == "__main__":
    app.run(debug=True)
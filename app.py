from flask import Flask, render_template, request, url_for, redirect
from data import read_student_by_student_id, read_student_by_house, update_student, insert_student, delete_student

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

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/processed', methods=['post'])
def processing():
    student_data = {
        "house": request.form['student_house'],
        "name": request.form['student_name'],
        "bday": request.form['student_bday'],
        "image": request.form['student_url'],
        "desc": request.form['student_desc'],
    }
    insert_student(student_data)
    return redirect(url_for('house', house = request.form['student_house']))

@app.route('/modify', methods = ['post'])
def modify():
    if request.form["modify"] == "Edit Student Profile":
        id = request.form["student_id"]
        student = read_student_by_student_id(id)
        return render_template("edit.html", student = student)
    elif request.form["modify"] == "Delete Profile":
        student_data = {
            "student_id":request.form["student_id"],}
        delete_student(student_data)
        return render_template('directory.html')

@app.route('/edit', methods=['post'])
def edit():
    student_data = {
        "student_id": request.form['student_id'],
        "name": request.form['student_name'],
        "house": request.form['student_house'],
        "bday": request.form['student_bday'],
        "image": request.form['student_url'],
        "desc": request.form['student_desc'],
    }
    update_student(student_data)
    return redirect(url_for('student', student_id = request.form['student_id']))

if __name__ == "__main__":
    app.run(debug=True)
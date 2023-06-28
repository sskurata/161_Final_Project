from flask import Flask, render_template
from data import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students/<house>')
def students(house):
    student_list = read_student_by_house(house)
    return render_template("students.html", house=house, students=student_list)

@app.route('/animals/<int:pet_id>')
def pet(pet_id):
    pet = read_pet_by_pet_id(pet_id)
    return render_template("pet.html",pet=pet)

if __name__ == "__main__":
    app.run(debug=True)
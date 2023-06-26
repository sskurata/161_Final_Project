from flask import Flask, render_template
from data import pets

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html'))

@app.route('/animals/<pet_type>')
def animals(pet_type):
    html = "<h1>List of {}</h1>".format(pet_type)
    html += "<ul>"

    for i,pet in enumerate(pets[pet_type]):
        html += "<li><a href='/animals/{}/{}'>{n}</a></li>".format(pet_type,i,n = pet["name"])

    html += "</ul>"


    return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]
    html = "<h1>{}</h1>".format(pet['name'])
    html += "<img src={}>".format(pet['url'])
    html += "<p>{}</p>".format(pet['description'])
    html += "<ul><li>Breed: {}</li><li>Age: {}</li></ul>".format(pet['breed'], pet['age'])
    return html

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Students')
def students():
    return render_template('students.html')

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, render_template
import pyrebase
from config import firebaseConfig

app = Flask(__name__)

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        branch = request.form['branch']

        data = {"name": name, "branch": branch}

        # Push data to Firebase
        db.child("students").push(data)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

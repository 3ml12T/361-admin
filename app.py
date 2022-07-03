from flask import Flask, render_template

app = Flask(__name__)


@app.route('/a')
def hello():
    return render_template('index.html')
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def page():
    return render_template('hello2019.html')
app.run(debug=True)
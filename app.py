from flask import Flask, jsonify, request, render_template

app = Flask(__name__, template_folder='Templates')


@app.route('/')
def hello():
    return render_template('homeFile.html')

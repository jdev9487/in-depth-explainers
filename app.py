from flask import Flask
from flask import send_file
import os

app = Flask(__name__)

@app.get("/pdf/<slug>")
def pdf(slug):
    filename = f'output/{slug}.pdf'
    return send_file(filename, mimetype='application/pdf')

@app.get("/pdf/metadata")
def all_metadata():
    return os.listdir("latex")

if __name__ == "__main__":
    app.run()
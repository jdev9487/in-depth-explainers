from flask import Flask
from flask import send_file
from pypdf import PdfReader
import os
import json

app = Flask(__name__)

@app.get("/pdf/<slug>")
def pdf(slug):
    filename = f'output/{slug}.pdf'
    return send_file(filename, mimetype='application/pdf')

@app.get("/pdf/metadata")
def all_metadata():
    metadata = list(map(lambda y: [y[0].author, y[0].subject, y[0].title, y[1]], [[PdfReader(os.path.join("output", x)).metadata, x] for x in os.listdir("output")]))
    data = []
    for m in metadata:
        entry = {}
        entry['user'] = m[0]
        entry['description'] = m[1]
        entry['title'] = m[2]
        entry['slug'] = m[3][:-4]
        data.append(entry)
    return json.dumps(data)

if __name__ == "__main__":
    app.run()
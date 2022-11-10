from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mushrooms'
app_data = {
    "name": "Mushroom Database",
    "description": "Website to explore the mushroom dataset",
    "author": "Victor Del Carpio, Samuel Tigistu",
    "html_title": "Mushroom Dataset",
    "project_name": "Mushroom Dataset",
    "keywords": ""
}

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", app_data = app_data)

if __name__ == '__main__':
    app.run(debug=True)

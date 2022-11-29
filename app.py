from flask import Flask, render_template
from website_utils import create_map, get_images
from flask_wtf import FlaskForm
from wtforms import SelectField
import folium

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

class MushroomForm(FlaskForm):
    genus = SelectField("Select Genus", choices=[("Amanita", "Amanita"), ("Cortinarius", "Cortinarius"), ("Entoloma", "Entoloma"), ("Hygrocybe", "Hygrocybe"), ("Lactarius", "Lactarius"), ("Russula", "Russula"), ("Suillus", "Suillus")])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MushroomForm()
    if form.validate_on_submit():
        choice: str = form.genus.data
        map_data: folium.Map = create_map(choice)
        return render_template("index.html", app_data = app_data, form=form, map_data = map_data._repr_html_(), img_data = get_images(choice))

    else:
        return render_template("index.html", app_data = app_data, form=form, map_data = None, img_data = [])

if __name__ == '__main__':
    app.run(debug = True)

import folium
from sklearn.utils import shuffle
import sqlite3
import os
import random
from PIL import Image

"""
Connect to both databases and get the latitude and longitude values
of all of the mushrooms of a specific genus.
"""
def create_map(genus: str) -> folium.Map:
    connection: sqlite3.Connection = sqlite3.connect('./databases/gbif.db')
    cursor: sqlite3.Cursor = connection.cursor()
    cursor.execute('ATTACH DATABASE "./databases/locations.db" AS locs')
    command: str = f"SELECT decimalLatitude, decimalLongitude\
        FROM locs.locations, mushrooms\
        WHERE (locations.uniqueID = mushrooms.uniqueID)\
        AND (mushrooms.genus = '{genus}')"
    cursor.execute(command)

    # Shuffle the values to show more geographic distribution
    points: list = cursor.fetchall()
    points = shuffle(points, random_state = 101)

    result: folium.Map = folium.Map(location = points[0], zoom_start = 10)
    
    max_points: int = min(500, len(points))
    for point in points[:max_points]:
        folium.Marker(point).add_to(result)
    
    connection.close()
    return result

def get_image(genus: str) -> Image:
    directory_path: str = f"./data/Mushrooms/{genus}/"
    directory: list = os.listdir(directory_path)
    filepath: str = random.choice(directory)
    image: Image = Image.open(f"{directory_path}{filepath}")
    return image
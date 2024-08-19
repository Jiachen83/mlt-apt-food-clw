import flask
import os
from api_food import get_recipes

app = flask.Flask(__name__)

@app.route('/')
def index():
    recipes = get_recipes()
    return flask.render_template("index.html", recipes=recipes)

if __name__ == '__main__':
    app.run(
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0'),
        debug=True
    )



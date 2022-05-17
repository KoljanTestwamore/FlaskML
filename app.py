import json
from operator import mod
from statistics import mode
import pandas as pd
from flask import Flask, jsonify, request, send_from_directory
from catboost import CatBoostRegressor, Pool
# load model
app = Flask(__name__)

model = CatBoostRegressor()
model.load_model("model")
labels = ['floor', 'open_plan', 'rooms', 'studio', 
         'area', 'kitchen_area', 'living_area']


# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@app.route("/predict", methods=["POST"])
def predict():
    data = json.loads(request.data)

    vals = pd.DataFrame([[
            data.get('floor'),
            False,
            data.get('rooms'),
            False,
            data.get('area'),
            data.get('area')/5,
            data.get('area')
        ]], columns=labels)

    return str(model.predict(vals)[0])

if __name__ == "__main__":
    app.run(debug=True)
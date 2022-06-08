import json
import pandas as pd
from flask import Flask, request, send_from_directory
from catboost import CatBoostRegressor

app = Flask(__name__)

model = CatBoostRegressor()
model.load_model("model")

model_original = CatBoostRegressor()
model_original.load_model("model_original")

labels = ['floor', 'open_plan', 'rooms', 'studio', 
         'area', 'kitchen_area', 'living_area']

labels_original = ['floor', 'open_plan', 'rooms', 'studio', 
                  'area', 'kitchen_area', 'living_area',
                  'renovation', 'agent_fee']

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

    if data.get('origModel'):
        vals = []
        for label in labels_original:
            vals.append(data.get('data').get(label))
        print(vals, len(vals))
        return str(model_original.predict(pd.DataFrame([vals], columns=labels_original))[0])
    else:
        vals = []
        for label in labels:
            vals.append(data.get('data').get(label))
        return str(model.predict(pd.DataFrame([vals], columns=labels))[0])

if __name__ == "__main__":
    app.run(debug=True)

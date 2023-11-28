import numpy as np
from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('models/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [np.array([float(x) for x in request.form.values()])]
    prediction = model.predict(features)
    result = prediction[0]
    print(features)

    return render_template('results.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
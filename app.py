# Epic 5: Story 2 - Core Flask Server Framework
from flask import Flask, render_template, request, redirect, url_for
import joblib
import pandas as pd
import numpy as np

# 1. Initialize Flask Application Instance
app = Flask(__name__)

# 2. Deserialization Interface: Load Model and Scaler Assets
try:
    model = joblib.load('floods.save')
    scaler = joblib.load('transform.save')
    print("SYSTEM LOG: Serialization assets loaded successfully.")
except Exception as e:
    print(f"SYSTEM CRITICAL ERROR LOADING ASSETS: {e}")

# 3. Page Routing Infrastructure
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        # Extraction logic for form parameter inputs
        try:
            rainfall_val = float(request.form['rainfall'])
            
            # Structuring inputs into an array matching 5 independent feature slots
            # Note: We duplicate or fill values if your specific model structure expects exactly 5 dimensions.
            input_features = np.array([[rainfall_val, 0.0, 0.0, 0.0, 0.0]])
            
            # Transform data matrices using loaded scaler logic
            scaled_features = scaler.transform(input_features)
            
            # Run prediction array using structural XGBoost engine
            prediction = model.predict(scaled_features)
            
            # Routing conditional pathways depending on classification binary mask (1 = Flood, 0 = Safe)
            if prediction[0] == 1:
                return redirect(url_for('chance'))
            else:
                return redirect(url_for('no_chance'))
                
        except Exception as err:
            print(f"ERROR DURING INFERENCE PIPELINE: {err}")
            return redirect(url_for('home'))

@app.route('/chance')
def chance():
    return render_template('chance.html')

@app.route('/no_chance')
def no_chance():
    return render_template('no_chance.html')

# 4. Engine Boot Sequence Configuration
if __name__ == '__main__':
    print("STARTING LOCAL APPLICATION DEPLOYMENT SERVER...")
    app.run(debug=True, port=5000)
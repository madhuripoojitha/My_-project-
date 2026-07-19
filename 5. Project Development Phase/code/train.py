# =====================================================================
# Epic 5: Core Flask Deployment Engine with Intelligent Risk Routing
# =====================================================================
from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import pandas as pd
import numpy as np

# 1. Initialize Flask Application Instance
app = Flask(__name__)
app.secret_key = 'smartbridge_secret_key_change_this_later'

# 2. Load Model and Scaler Assets
try:
    model = joblib.load('floods.save')
    scaler = joblib.load('transform.save')
    print("SYSTEM LOG: Serialization assets loaded successfully.")
except Exception as e:
    print(f"SYSTEM CRITICAL ERROR LOADING ASSETS: {e}")


# ==========================================
# --- SECTION A: AUTHENTICATION GATEWAYS ---
# ==========================================

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if email == "admin@flood.com" and password == "password123":
            session['logged_in'] = True
            session['user_email'] = email
            session['user_role'] = "Disaster Management Officer"
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid credentials. Try admin@flood.com / password123")
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


# ==========================================
# --- SECTION B: CORE APPLICATION ROUTES ---
# ==========================================

@app.route('/')
def home():
    is_logged_in = session.get('logged_in', False)
    return render_template('home.html', is_logged_in=is_logged_in)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        try:
            # 1. Extract values from index.html form
            rainfall_val = float(request.form['rainfall'])
            
            # 2. Shape input into a 10-feature array matching your scaler structure
            input_features = np.array([[rainfall_val, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])
            
            # 3. Transform inputs through your scaler matrix
            scaled_features = scaler.transform(input_features)
            
            # 4. Generate prediction array index
            prediction = model.predict(scaled_features)[0]
            
            # 5. Route dynamic risk logic warnings (with fallback threshold protection)
            if prediction == 1 or rainfall_val > 300:
                if rainfall_val > 3000:
                    risk_level = "CRITICAL RISK: Immediate Flood Warning Protocol Active!"
                    css_class = "risk-critical"
                else:
                    risk_level = "MODERATE RISK: Elevated Water Levels Detected. Monitor Local Channels."
                    css_class = "risk-moderate"
            else:
                risk_level = "STABLE: Environmental parameters are within normal safe thresholds."
                css_class = "risk-stable"
            
            return render_template('result.html', risk=risk_level, alert_style=css_class, rainfall=rainfall_val)
                
        except Exception as err:
            # CRITICAL: If the pipeline fails, print the explicit error on screen 
            return f"<h2 style='color:red;'>Inference Pipeline Failed!</h2><p><strong>Error Details:</strong> {err}</p><p><a href='/predict'>Go Back</a></p>"


# ==========================================
# --- SECTION C: BOOT SEQUENCE & HOSTING ---
# ==========================================

if __name__ == '__main__':
    print("STARTING LOCAL APPLICATION DEPLOYMENT SERVER...")
    # Using Port 7000 as configured on your workstation environment
    app.run(debug=True, port=7000, use_reloader=False)
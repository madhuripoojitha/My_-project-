# Rising Waters: Machine Learning-Based Flood Prediction System

Rising Waters is an end-to-end Machine Learning deployment pipeline designed to predict regional flood risks based on environmental and rainfall data metrics. The system utilizes an advanced ensemble learning backend integrated seamlessly with a lightweight Flask web application to deliver real-time public safety risk routing assessments.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##QUICK START / ACTIVATION CODE

Whenever your Codespace restarts or deactivates, copy and paste this single line into your terminal to instantly launch the application: bash

# Shift focus to project directory root
cd "C:/Users/DHARANI/OneDrive/Documents/Rising Waters"

# Activate the local web deployment server
python app.py

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Verification & Live URL Mapping
Once the system logs verify that serialization assets have loaded cleanly, access the local port configuration in your web browser:
URL Destination: [http://127.0.0.1:7000/](http://127.0.0.1:7000/)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🚀 Core Features

* **Multi-Model Machine Learning Engine**: Features modular validation modules for Decision Trees, Random Forests, K-Nearest Neighbors (KNN), and XGBoost.
* **Production XGBoost Integration**: Utilizes a highly optimized Gradient Boosting infrastructure achieving **96.55% validation accuracy**.
* **Intelligent Risk Routing**: Built-in algorithmic fallback loops that dynamically categorize risk into Stable, Moderate, or Critical warning pipelines based on ingestion parameters.
* **Secure Access Controls**: Role-based access gateways protecting core predictive tools from unauthorized exposure.

---

## 📂 Repository Architecture

```text
Rising Waters/
│
├── app.py                  # Core Flask backend and route coordinator
├── flood_prediction.ipynb  # Data preprocessing, training, and benchmarking matrix
├── floods.save             # Serialized production XGBoost model artifact
├── transform.save          # Serialized StandardScaler matrix configurations
│
├── templates/              # HTML Presentation View Layers
│   ├── home.html           # System landing portal
│   ├── login.html          # Administrative authentication portal
│   ├── index.html          # Environmental data parameter ingestion form
│   └── result.html         # Dynamic risk report output UI
│
└── static/                 # Frontend Asset Components
    ├── main.css            # Responsive layout and alert stylesheets
    └── main.js             # Client-side validation mechanics

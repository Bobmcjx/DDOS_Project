# DDOS Analysis Kit

## Overview
DDOS Analysis Kit is a Python-based application that helps detect DDOS attacks from network packet capture (PCAP) files. It utilizes machine learning to classify network traffic as either a DDOS attack or normal activity.

## Features
- Graphical User Interface (GUI) built with Tkinter
- Supports PCAP file analysis
- Uses a pre-trained Random Forest model for DDOS detection
- Provides real-time analysis results

## Installation
### Prerequisites
Ensure you have Python 3 installed. The required dependencies are listed in `requirements.txt`.

### Install Dependencies
Run the following command to install all necessary packages:
```bash
pip install -r requirements.txt
```

## Usage
1. Run the application:
   ```bash
   python app.py
   ```
2. Select a PCAP file for analysis.
3. Click on "Send Request" to start the analysis.
4. The result will be displayed on the screen.

## Project Structure
```
DDOS_Project/
│── app.py              # GUI application
│── ddos_engine.py      # DDOS detection engine
│── random_forest_model.pkl  # Trained machine learning model
│── standard_scaler.pkl # Scaler for data normalization
│── requirements.txt    # Dependencies
│── DDoS.png           # Logo/image for UI
```

## How It Works
1. `app.py` provides a user-friendly interface for selecting files and viewing results.
2. `ddos_engine.py` loads the trained model and processes the input PCAP file.
3. The model predicts whether the network activity is a DDOS attack or not.

## Model Details
- The machine learning model is a **Random Forest Classifier**.
- The model was trained using `scikit-learn 1.6.1`.
- The `standard_scaler.pkl` is used to normalize features before making predictions.

## Troubleshooting
If you encounter version compatibility issues while loading the model, try using the exact versions in `requirements.txt`:
```bash
pip install -r requirements.txt
```

If the issue persists, you may need to retrain the model using the current `scikit-learn` version.

## License
This project is open-source and available under the MIT License.
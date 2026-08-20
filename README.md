# 🚗 Car Price Prediction API & Streamlit Dashboard

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)

A full-stack Machine Learning application for predicting used car selling prices. Built with **FastAPI** for a robust RESTful API backend, **Scikit-Learn (Random Forest)** for inference, and an interactive **Streamlit** web application for frontend user interaction.

---

## 🌟 Key Features

- **Machine Learning Pipeline**: Trained using a `RandomForestRegressor` model with standard one-hot encoding on categorical attributes.
- **RESTful API**: Fast and asynchronous backend powered by **FastAPI** and **Pydantic v2** for input validation.
- **Interactive UI**: Clean, responsive frontend built with **Streamlit** featuring instant prediction calculations.
- **Dual Server Mode**: Streamlit UI includes a sidebar configuration to switch between **Local FastAPI** and **Production Render** API endpoints.
- **Auto OpenAPI Docs**: Swagger UI documentation generated automatically at `/docs`.

---

## 📁 Repository Structure

```text
car-price-api/
├── main.py                   # FastAPI application & route handlers
├── model.py                  # Model loading & preprocessing pipeline
├── schema.py                 # Pydantic data schemas & Enums validation
├── streamlit_app.py          # Interactive Streamlit frontend UI
├── train.py                  # Script to train Random Forest model on dataset
├── cardekho_data (1).csv     # CarDekho vehicle sales dataset
├── random_forest_model.pkl   # Serialized Random Forest model artifact
├── feature_columns.pkl       # Serialized feature column alignment order
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 🛠️ Installation & Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yoloaryan/car-price-api.git
cd car-price-api
```

### 2. Create a Virtual Environment & Install Dependencies
```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

---

## 🚀 Running Locally

To run the complete application locally, open **two terminal windows**:

### Terminal 1: Start the FastAPI Backend
```bash
uvicorn main:app --reload
```
- The API will start at: `http://127.0.0.1:8000`
- View Interactive API Docs (Swagger): `http://127.0.0.1:8000/docs`

### Terminal 2: Start the Streamlit Frontend
```bash
streamlit run streamlit_app.py
```
- The web app will open at: `http://localhost:8501`

---

## 📡 API Endpoint Reference

### `POST /predict`

Calculates the estimated selling price of a car based on input vehicle features.

#### **Request Body Example (`application/json`)**:
```json
{
  "Car_Name": "swift",
  "Year": 2014,
  "Present_Price": 5.59,
  "Kms_Driven": 27000,
  "Fuel_Type": "Petrol",
  "Seller_Type": "Dealer",
  "Transmission": "Manual",
  "Owner": 0
}
```

#### **Response Example (`200 OK`)**:
```json
{
  "prediction_price": 3.806
}
```

#### **Field Constraints**:
- `Fuel_Type`: `"Petrol"`, `"Diesel"`, or `"CNG"`
- `Seller_Type`: `"Dealer"` or `"Individual"`
- `Transmission`: `"Manual"` or `"Automatic"`
- `Owner`: Integer between `0` and `3`

---

## ☁️ Deployment

### Backend (Render)

->

The FastAPI backend is deployed on Render at:
`https://car-price-api-86h5.onrender.com`

- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

> **Note**: Render free tier instances spin down after 15 minutes of inactivity. First requests after idle periods may take 30–50 seconds to wake up the server (cold-start).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

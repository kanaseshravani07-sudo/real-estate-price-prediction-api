# 🏡 Real Estate Price Prediction API

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge\&logo=scikitlearn\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge\&logo=pandas\&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

<p align="center">
A production-ready <strong>Machine Learning REST API</strong> built with <strong>FastAPI</strong> that predicts California real estate prices using a trained <strong>Random Forest Regressor</strong>.
</p>

---

## ✨ Features

* 🚀 High-performance REST API using FastAPI
* 🤖 Random Forest Regression model
* ✅ Input validation with Pydantic
* 📊 Predict real estate prices instantly
* 📄 Interactive Swagger & ReDoc documentation
* ⚡ Fast inference using Joblib
* 🛡️ Structured error handling

---

# 🛠️ Tech Stack

| Technology      | Purpose                   |
| --------------- | ------------------------- |
| 🐍 Python       | Core Programming Language |
| ⚡ FastAPI       | REST API Framework        |
| 🤖 Scikit-learn | Machine Learning Model    |
| 🐼 Pandas       | Data Processing           |
| 📦 Joblib       | Model Serialization       |
| ✅ Pydantic      | Request Validation        |
| 🚀 Uvicorn      | ASGI Server               |

---

# 📂 Project Structure

```text
real-estate-price-prediction-api/
│
├── main.py
├── train.py
├── explore.py
├── requirements.txt
├── README.md
├── .gitignore
├── house_model.joblib
└── house_features.joblib
```

---

# 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/kanaseshravani07-sudo/real-estate-price-prediction-api.git
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

### 3️⃣ Activate Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Train the Model

```bash
python train.py
```

### 6️⃣ Run the API

```bash
uvicorn main:app --reload
```

---

# 🌐 API Endpoints

| Method | Endpoint   | Description         |
| ------ | ---------- | ------------------- |
| GET    | `/`        | API Status          |
| GET    | `/health`  | Health Check        |
| POST   | `/predict` | Predict House Price |

---

# 🧪 Sample Request

```json
{
  "MedInc": 8.32,
  "HouseAge": 41,
  "AveRooms": 6.98,
  "AveBedrms": 1.02,
  "Population": 322,
  "AveOccup": 2.56,
  "Latitude": 37.88,
  "Longitude": -122.23
}
```

---

# 📤 Sample Response

```json
{
  "Predicted_Price": "$414,719",
  "Model_Output": 4.15,
  "Confidence_Range": "$375,719 - $453,719"
}
```

---

# 📖 API Documentation

Once the server is running:

🔹 **Swagger UI**

```text
http://127.0.0.1:8000/docs
```

🔹 **ReDoc**

```text
http://127.0.0.1:8000/redoc
```

---

# 📈 Future Improvements

* 🐳 Docker Support
* ☁️ Cloud Deployment
* 🔐 Authentication
* 📊 Model Monitoring
* 🧪 Unit Testing
* 🔄 CI/CD Pipeline

---

# 👩‍💻 Author

**Shravani Kanase**

⭐ If you found this project useful, consider giving it a star!

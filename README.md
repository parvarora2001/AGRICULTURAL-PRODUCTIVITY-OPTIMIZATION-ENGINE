# Agricultural Productivity Optimization Engine

A machine learning-based crop recommendation system that predicts the most suitable crop to grow based on soil composition and environmental conditions. Built with Python and scikit-learn, with an interactive Jupyter notebook for analysis and a Flask web application for deployment.

---

## Overview

The engine analyses 7 key soil and environmental parameters to recommend the optimal crop from 22 possible crops. It combines exploratory data analysis, clustering, and classification to give farmers and agricultural experts data-driven planting recommendations.

---

## Project Structure

```
AGRICULTURAL-PRODUCTIVITY-OPTIMIZATION-ENGINE/
├── Agricultural Productivity Optimization Engine.ipynb  # Full ML pipeline notebook
├── app.py                                               # Flask web application
├── agriculture_data.csv                                 # Dataset (2200 records, 22 crops)
└── sample.txt                                           # Frontend crop selector HTML snippet
```

---

## Dataset

**File:** `agriculture_data.csv`
**Records:** 2,200
**Crops:** 22

| Feature | Description |
|---|---|
| `N` | Nitrogen content in soil |
| `P` | Phosphorus content in soil |
| `K` | Potassium content in soil |
| `temperature` | Temperature in °C |
| `humidity` | Relative humidity (%) |
| `ph` | Soil pH value |
| `rainfall` | Rainfall in mm |
| `label` | Recommended crop (target variable) |

### Supported Crops

Rice, Maize, Chickpea, Kidney Beans, Pigeon Peas, Moth Beans, Mung Bean, Black Gram, Lentil, Pomegranate, Banana, Mango, Grapes, Watermelon, Muskmelon, Apple, Orange, Papaya, Coconut, Cotton, Jute, Coffee

---

## Notebook Walkthrough

### 1. Data Cleaning
- Checks for null values (none found in the dataset)
- Renames columns for readability (`N → Nitrogen`, `P → Phosphorus`, `K → Potassium`)

### 2. Exploratory Data Analysis
- Computes average soil and environmental conditions per crop
- Interactive widgets (`ipywidgets`) to compare conditions across all 22 crops
- Identifies crops requiring extreme conditions — very high/low nitrogen, pH, rainfall, temperature
- Categorises crops by season: Summer, Winter, Rainy

### 3. Clustering
- KMeans clustering applied to group crops by similar growing conditions
- Elbow method used to determine the optimal cluster count (k=4)

### 4. Predictive Modelling
- **Model:** Logistic Regression
- **Split:** 80% training / 20% testing (`random_state=0`)
- **Input:** 7 soil and environment features
- **Output:** Recommended crop label
- Evaluated using `classification_report` and `accuracy_score`

### 5. Prediction
- Single prediction: pass an array of 7 values to get a crop recommendation
- Interactive CLI loop: prompts the user for each parameter and returns the recommended crop

---

## Prerequisites

```bash
pip install pandas numpy matplotlib seaborn scikit-learn ipywidgets flask
```

---

## Running the Notebook

```bash
jupyter notebook "Agricultural Productivity Optimization Engine.ipynb"
```

Run all cells in order. The interactive `@interact` widgets in the EDA section allow exploring crop statistics by selecting from a dropdown.

**Example prediction:**
```python
prediction = model.predict(np.array([[90, 40, 40, 30, 60, 7, 200]]))
# Output: ['rice']
```

---

## Running the Flask App

```bash
python app.py
```

App runs at `http://127.0.0.1:5000`

### Endpoints

| Method | Route | Description |
|---|---|---|
| `GET` | `/` | Renders the main UI (`index.html`) |
| `POST` | `/crop_summary` | Accepts selected crop from dropdown, returns crop name |

The frontend uses a dropdown with all 22 supported crops. On form submit, the selected crop value is posted to `/crop_summary`.

---

## Tech Stack

| Component | Technology |
|---|---|
| Data Analysis | Pandas, NumPy |
| Visualisation | Matplotlib, Seaborn |
| Interactive Widgets | ipywidgets |
| ML — Clustering | scikit-learn KMeans |
| ML — Classification | scikit-learn Logistic Regression |
| Web Framework | Flask |
| Notebook | Jupyter |

---

## Future Enhancements

- Add Decision Tree, Random Forest, and Gradient Boosting models for comparison
- Add fertiliser and irrigation recommendations based on predicted crop
- Build out the full frontend UI with input fields for all 7 parameters
- Deploy to cloud (Heroku / AWS / GCP)
- Integrate a weather API for real-time environmental data input

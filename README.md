# Gym Training Pipeline — End-to‑End ML Project (Data → Model → App)

A compact, CV‑ready project that demonstrates a full machine‑learning lifecycle for strength‑training data. It ingests workout sessions from a SQLite database (seeded from JSON), engineers features, trains and selects regression models, serializes the winning model + preprocessing pipeline, and serves live predictions via a minimal Flask web app.

> **Use case**: Predict exercise (default: bench press) **volume** (weight × reps) from session context (anthropometrics, sleep, stress, mood, program phase, etc.).

---

## Key Features

* **Real dataset & storage**: SQLite (`workout_data_base.db`) with a normalized schema; seed via `data.json`.
* **Reproducible ingestion**: `analysis/dataframe_builder.py` builds a clean Pandas DataFrame directly from SQL joins.
* **Modular ML pipeline**:

  * Separate components for **ingestion**, **transformation**, and **model training** (`src/components/*`).
  * Robust preprocessing with **imputation**, **standardization**, and **one‑hot encoding** using `ColumnTransformer`.
  * Multiple regressors (CatBoost, XGBoost, RandomForest, GradientBoosting, etc.) evaluated and grid‑searched.
* **Model packaging**: Persisted artifacts (`artifacts/model.pkl`, `artifacts/preprocessor.pkl`) for portable inference.
* **Web UI**: Flask app with a simple form (`/predictdata`) → returns predicted bench‑press volume.
* **Logging**: Centralized `logging` to timestamped files in `logs/`.

---

## Project Structure

```
.
├─ app.py                         # Flask app (routes: '/', '/predictdata')
├─ analysis/
│  ├─ dataframe_builder.py        # SQL → DataFrame builder (joins sessions + exercises)
│  ├─ model_training.ipynb        # Notebook for exploratory training
│  └─ user_analysis.ipynb         # (Optional) EDA / analysis
├─ database/
│  ├─ __init__.py                 # SQLite connection + init
│  ├─ schema.sql                  # Users, training_sessions, exercises
│  ├─ data_loader.py              # Seed DB from data.json
│  ├─ queries.py                  # Query helpers (incl. training dataset)
│  ├─ users.py, sessions.py, exercises.py
├─ src/
│  ├─ exception.py, logger.py, utils.py
│  ├─ components/
│  │  ├─ data_ingestion.py        # Read/partition data; orchestrates transform + train
│  │  ├─ data_transformation.py   # numerical + categorical pipelines
│  │  └─ model_trainer.py         # model zoo + GridSearchCV + reporting
│  └─ pipeline/
│     ├─ predict_pipeline.py      # loads artifacts; defines `CustomData`
│     └─ train_pipeline.py        # (placeholder for CLI training entrypoint)
├─ templates/
│  ├─ index.html                  # landing page
│  └─ home.html                   # prediction form & result card
├─ database_init.py               # one‑shot: init schema + load data.json
├─ data.json                      # demo dataset (users & sessions)
├─ requirements.txt               # core dependencies
└─ workout_data_base.db           # SQLite database (generated)
```

---

## Data Model (SQLite)

**Tables**

* `users (id, name, email)`
* `training_sessions (id, user_id, training_day, body_weight, mood, date, dchest, arms, waist, legs, shoulders, training_duration_minutes, sleep_hours, stress_level, program_phase)`
* `exercises (id, session_id, exercise, muscle_group, weight, reps)`

**Training view** (joined via `analysis/dataframe_builder.py`):

* Adds `volume = weight * reps` as target.

---

## ML Pipeline

1. **Ingestion** (`src/components/data_ingestion.py`)

   * Optionally filters by exercise (e.g., *Barbell Bench Press*).
   * Train/validation split with `train_test_split`.
2. **Transformation** (`src/components/data_transformation.py`)

   * Numerical: `SimpleImputer(strategy="median" or "mean")` → `StandardScaler`.
   * Categorical: `SimpleImputer("most_frequent")` → `OneHotEncoder(handle_unknown="ignore")` → `StandardScaler(with_mean=False)`.
   * Combined via `ColumnTransformer`.
3. **Modeling** (`src/components/model_trainer.py`)

   * Model zoo: `CatBoostRegressor`, `XGBRegressor`, `RandomForestRegressor`, `GradientBoostingRegressor`, `DecisionTreeRegressor`, `LinearRegression`, `KNeighborsRegressor`, `AdaBoostRegressor`.
   * Hyperparameter search with `GridSearchCV` (per‑model grids).
   * Metric: `r2_score` (can be extended to MAE/RMSE).
   * Best model + params reported and **saved**.
4. **Serialization** (`src/utils.py`)

   * `save_object()`/`load_object()` using `pickle` → `artifacts/`.
5. **Serving** (`src/pipeline/predict_pipeline.py`, `app.py`)

   * `CustomData` wraps form inputs → Pandas DataFrame.
   * `PredictPipeline` loads `preprocessor.pkl` + `model.pkl` and outputs a numeric volume prediction.

---

## Web App (Flask)

* **Routes**

  * `GET /` – landing page with CTA to prediction form.
  * `GET/POST /predictdata` – HTML form collecting features → shows predicted volume.
* **Inputs** (subset; can be extended):

  * `body_weight`, `mood`, `dchest`, `arms`, `waist`, `legs`, `shoulders`, `training_duration_minutes`, `sleep_hours`, `stress_level`, `program_phase`.

---

## Getting Started

### 1) Setup

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

### 2) Initialize the database (optional if `workout_data_base.db` already exists)

```bash
python database_init.py   # creates schema + loads demo records from data.json
```

### 3) (Re)Train models (optional)

> The project includes component code for training; you can wire a simple CLI in `src/pipeline/train_pipeline.py` to call `DataTransformation` and `ModelTrainer`.

Example (pseudo‑CLI inside a `train()` function):

```python
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

train_csv, test_csv = DataIngestion().initiate_data_ingestion()
train_arr, test_arr, _ = DataTransformation().initiate_data_transformation(train_csv, test_csv)
print(ModelTrainer().initiate_model_trainer(train_arr, test_arr))
```

Artifacts will appear under `artifacts/` as `preprocessor.pkl` and `model.pkl`.

### 4) Run the web app

```bash
python app.py
# open http://127.0.0.1:5000
```

---

## Tech Stack

* **Language**: Python (3.10+)
* **ML**: scikit‑learn, XGBoost, CatBoost
* **Data**: Pandas, SQLite3
* **App**: Flask + Jinja2 templates
* **Tooling**: logging, GridSearchCV, pickle‑based artifacting

---

## What This Project Demonstrates (CV Highlights)

* Designing a **normalized schema** for fitness data and wiring **ETL** from SQLite → Pandas.
* Building a **modular, testable** ML pipeline with clear component boundaries.
* Performing **model selection** with hyperparameter search across gradient‑boosting and tree‑based methods.
* **Packaging** model + preprocessing for **production‑style** inference.
* Delivering a **user‑facing app** that consumes the model via a simple HTTP interface.

---

## Notes & Extensibility

* `src/pipeline/train_pipeline.py` is a placeholder; add a CLI (e.g., `argparse`) for repeatable training.
* Add input validation and a thin schema layer (e.g., `pydantic`) to harden the Flask form.
* Consider switching serialization to `joblib` or a model registry if the project grows.
* Expand metrics to MAE/RMSE; add cross‑validation and learning‑curve plots.

---

## How to Talk About It (Interview Script)

* *“This is an end‑to‑end ML demo: I designed the data model, built a Pandas ETL, evaluated multiple regressors with GridSearchCV, tracked performance with R², serialized the best model + preprocessing, and exposed it via Flask. The code splits concerns into ingestion, transformation, modeling, and serving, which made it easy to iterate and reason about.”*

---

## Requirements

See `requirements.txt` for the full list. Key packages: `numpy`, `pandas`, `scikit-learn`, `catboost`, `xgboost`, `flask`.

---

## License

MIT.

---


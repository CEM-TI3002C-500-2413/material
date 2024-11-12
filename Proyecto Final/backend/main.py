import joblib
import sqlite3
import pandas as pd
from datetime import date
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Literal

class RestaurantSearchModel(BaseModel):
    terms: str
    
class RestaurantTransactionsModel(BaseModel):
    restaurant_id: int
    start_date: date
    end_date: date
    
class PredictionModel(BaseModel):
    food_type: str
    smoking_area: Literal["Yes", "No"]
    price_range: Literal["$", "$$", "$$$", "$$$$"]
    city: str
    state: str

def create_connection():
    conn = sqlite3.connect("data.db")
    return conn

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

def load_regression_model():
    return joblib.load("lr_model.joblib")

def load_classification_model():
    return joblib.load("rf_model.joblib")

app = FastAPI()

@app.get("/food_types")
def food_types():
    conn = create_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    query = "SELECT DISTINCT \"Food Type\" FROM restaurants ORDER BY \"Food Type\""
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

@app.get("/states")
def states():
    conn = create_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    query = "SELECT DISTINCT State FROM restaurants ORDER BY State"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

@app.get("/price_ranges")
def price_ranges():
    conn = create_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    query = "SELECT DISTINCT \"Price Range\" FROM restaurants ORDER BY \"Price Range\""
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

@app.post("/restaurant_search")
def restaurant_search(search: RestaurantSearchModel):
    conn = create_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    terms = search.terms.split()
    terms = " OR ".join(terms)
    query = "SELECT rowid, Name FROM restaurants_fts WHERE restaurants_fts MATCH ? ORDER BY rank"
    cursor.execute(query, (f"{terms}",))
    results = cursor.fetchall()
    conn.close()
    return results

@app.get("/restaurant/{restaurant_id}")
def restaurant(restaurant_id: int):
    conn = create_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    query = "SELECT  r.* FROM restaurants r WHERE r.ID = ?"
    cursor.execute(query, (restaurant_id, ))
    results = cursor.fetchone()
    conn.close()
    return results

@app.get("/restaurant/{restaurant_id}/image", response_class=FileResponse)
def restaurant_image(restaurant_id: int):
    conn = create_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    query = "SELECT Image FROM restaurants WHERE ID = ?"
    cursor.execute(query, (restaurant_id, ))
    results = cursor.fetchone()
    conn.close()
    return FileResponse(f"images/{results["Image"]}")

@app.post("/transactions")
def restaurant_transactions(transactions: RestaurantTransactionsModel):
    conn = create_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    query = """
    SELECT t.*
    FROM transactions t
    JOIN waiters w ON t.Waiter = w.ID
    WHERE w.Restaurant = ?
    AND t.Timestamp BETWEEN ? AND ?;
    """
    cursor.execute(query, (transactions.restaurant_id, transactions.start_date, transactions.end_date))
    results = cursor.fetchall()
    conn.close()
    return results

@app.post("/predict")
def predict(prediction: PredictionModel):
    lr_model = load_regression_model()
    rf_model = load_classification_model()
    pred_df = pd.DataFrame([{
        "Food Type": prediction.food_type,
        "Smoking Area": prediction.smoking_area,
        "Price Range": prediction.price_range,
        "City": prediction.city,
        "State": prediction.state
    }])
    lr_model_pred = lr_model.predict(pred_df)[0]
    rf_model_pred = rf_model.predict(pred_df)[0]
    return {"monthly_tip_average": lr_model_pred, "classification": rf_model_pred}

@app.post("/predict_file")
def predict_file(file: UploadFile = File(...)):
    pred_df = pd.read_csv(file.file)
    lr_model = load_regression_model()
    rf_model = load_classification_model()
    pred_df["Monthly Tip Average"] = lr_model.predict(pred_df)
    pred_df["Classification"] = rf_model.predict(pred_df)
    return pred_df.to_dict(orient="records")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
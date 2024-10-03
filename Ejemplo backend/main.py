import pandas as pd
import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

class RestaurantModel(BaseModel):
    id : int
    restaurant : str
    food_type : str
    price_range : str
    rating : float = 0
    
def create_connection():
    conn = sqlite3.connect("data.db")
    return conn

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

app = FastAPI()
df = pd.read_csv("restaurants.csv")

@app.get("/")
def get_home():
    return {"mensaje": "Hola, éste es mi servidor"}

# Path parameter
@app.get("/food_type/{type}")
def get_food_type(type : str):
    return df[df["food type"] == type].to_dict(orient="records")

# Query parameter
@app.get("/restaurants")
def get_restaurants(col : str = "id", order : str = "asc"):
    if col not in df.columns: 
        col = "id"
    ascending = False if order == "desc" else True
    return df.sort_values(by = col, ascending=ascending).to_dict(orient="records")

@app.post("/restaurant")
def post_restaurant(restaurant : RestaurantModel):
    return {
        "id": restaurant.id,
        "restaurant": restaurant.restaurant,
        "food type": restaurant.food_type,
        "price range": restaurant.price_range,
        "rating": restaurant.rating
    }

# Respuesta como tupla
@app.get("/restaurant/{restaurant_id}")
def get_restaurant(restaurant_id : int):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM restaurant WHERE id = {restaurant_id}")
    result = cursor.fetchone()
    return result

# Dictionary Factory
@app.get("/restaurant_dict_factory/{restaurant_id}")
def get_restaurant(restaurant_id : int):
    conn = create_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM restaurant WHERE id = {restaurant_id}")
    result = cursor.fetchone()
    return result

# Pandas DataFrame
@app.get("/restaurant_dataframe/{restaurant_id}")
def get_restaurant(restaurant_id : int):
    conn = create_connection()
    result_df = pd.read_sql(f"SELECT * FROM restaurant WHERE id = {restaurant_id}", conn)
    return result_df.to_dict(orient="records")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
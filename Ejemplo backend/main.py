import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

class RestaurantModel(BaseModel):
    id : int
    restaurant : str
    food_type : str
    price_range : str
    rating : float = 0

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
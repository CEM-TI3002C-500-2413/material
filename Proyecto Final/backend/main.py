import sqlite3
from datetime import date
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

class RestaurantSearchModel(BaseModel):
    terms: str
    
class RestaurantTransactionsModel(BaseModel):
    restaurant_id: int
    start_date: date
    end_date: date

def create_connection():
    conn = sqlite3.connect("data.db")
    return conn

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

app = FastAPI()

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
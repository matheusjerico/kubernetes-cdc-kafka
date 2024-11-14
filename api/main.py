from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
from mysql.connector import Error

app = FastAPI()

# Database connection function
def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host="mysql.mysql.svc.cluster.local",
            user="cdc_user",
            password="cdc_password",
            database="cdc_db"
        )
        return connection
    except Error as e:
        print("Error connecting to MySQL database:", e)
        return None

# Pydantic model for the API request body
class Item(BaseModel):
    item_id: int
    name: str
    description: str

@app.post("/items/")
async def create_item(item: Item):
    """
    Endpoint to insert a new item into the MySQL database.
    
    Args:
    - item (Item): Item object containing item_id, name, and description.
    
    Returns:
    - dict: Success message or error message.
    """
    connection = create_db_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Failed to connect to the database.")
    
    try:
        cursor = connection.cursor()
        query = "INSERT INTO items (item_id, name, description) VALUES (%s, %s, %s)"
        cursor.execute(query, (item.item_id, item.name, item.description))
        connection.commit()
        return {"message": "Item created successfully"}
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

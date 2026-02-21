from fastapi import FastAPI, Form, Request, HTTPException, Body
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import mysql.connector
from typing import Dict, Any, List
import uuid

import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("Current working directory:", os.getcwd())
print("Base dir:", BASE_DIR)
print("Files in base dir:", os.listdir(BASE_DIR))

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static"
)

templates = Jinja2Templates(
    directory=os.path.join(BASE_DIR, "templates")
)
def get_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Manad@2007"
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("CREATE DATABASE IF NOT EXISTS cargosync")
        conn.database = "cargosync"
        return conn, cursor
    except Exception as e:
        print("DB Connection Error:", e)
        return None, None

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(
    request: Request,
    role: str = Form(...),
    username: str = Form(...),
    password: str = Form(...)
):
    if role == "Manager" and username == "abc@123" and password == "123":
        return RedirectResponse(url="/Dashboard.html", status_code=303)
    return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid Credentials"})

@app.get("/{page}.html")
def render_page(request: Request, page: str):
    conn, cursor = get_db()
    data = []
    if conn and cursor:
        try:
            cursor.execute(f"SELECT * FROM `{page}`")
            data = cursor.fetchall()
        except:
            pass # Table might not exist yet
        finally:
            cursor.close()
            conn.close()
    return templates.TemplateResponse(f"{page}.html", {"request": request, "data": data})

@app.post("/{page}.html")
async def handle_post(request: Request, page: str):
    form_data = await request.form()
    form_dict = dict(form_data)
    
    conn, cursor = get_db()
    if conn and cursor and form_dict:
        try:
            cols = []
            for k in form_dict.keys():
                cols.append(f"`{k}` VARCHAR(255)")
            cols_str = ", ".join(cols)
            
            cursor.execute(f"CREATE TABLE IF NOT EXISTS `{page}` (id INT AUTO_INCREMENT PRIMARY KEY, {cols_str})")
            
            # Check existing columns to add missing ones
            cursor.execute(f"SHOW COLUMNS FROM `{page}`")
            existing_cols = [row['Field'] for row in cursor.fetchall()]
            for k in form_dict.keys():
                if k not in existing_cols:
                    cursor.execute(f"ALTER TABLE `{page}` ADD COLUMN `{k}` VARCHAR(255)")
            
            keys = list(form_dict.keys())
            vals = list(form_dict.values())
            keys_str = ", ".join([f"`{k}`" for k in keys])
            placeholders = ", ".join(["%s"] * len(vals))
            
            cursor.execute(f"INSERT INTO `{page}` ({keys_str}) VALUES ({placeholders})", vals)
            conn.commit()
        except Exception as e:
            print(f"Error saving to {page}: {e}")
        finally:
            cursor.close()
            conn.close()

    return RedirectResponse(url=f"/{page}.html", status_code=303)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

from fastapi import FastAPI

app=FastAPI()

@app.get("/home")
def home():
    return {"success":True,"message":"Helllo World !"}

@app.get("/about")
def about():
    return{"Name":"Raj", "Location":"Mumbai"}

from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {"message":"task crud api is running"}
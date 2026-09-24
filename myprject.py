from fastapi import FastAPI
app=FastAPI()

@app.get("/user")
def show():
    return "hello world"
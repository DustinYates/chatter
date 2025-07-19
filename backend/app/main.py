from fastapi import FastAPI
from firebase_admin import credentials, initialize_app
print('------------TEST-----------------')
cred = credentials.Certificate("backend/firebase-admin-key.json")
initialize_app(cred)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Firebase is working!"}

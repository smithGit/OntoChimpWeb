"""
main.py for OntoChimpWeb - Initial FastAPI module for testing

2026-07-29 SMS Initial main.py for OntoChimpWeb

Folder: cd "D:\OntoChimpWeb"
conda activate env_python314
Execute: uvicorn main:app

"""
from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "OntoChimp Online",
        "version": "0.1"
    }
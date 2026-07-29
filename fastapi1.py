"""
fastapi1.py - first app for OntoChimpWeb

2026-07-29 SMS following creation of first App Service

"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "OntoChimp Online",
        "version": "0.1"
    }
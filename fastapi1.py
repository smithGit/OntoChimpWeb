"""
fastapi1.py - first app for OntoChimpWeb

2026-07-29 SMS following creation of first App Service
Folder: cd "D:\\OntoChimpWeb"
conda activate python314
Execute: python -m fastapi1
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "OntoChimp Online",
        "version": "0.1"
    }

@app.get("/ocw_version")
def show_version():
    return {
        "version": "OCW_v0.1"
    }
"""
main_min.py for OntoChimpWeb - Minimal FastAPI module to test locally

2026-07-29 SMS Initial main.py for OntoChimpWeb
2026-08-02 SMS adapted to exclude any DB access, simple items

Folder: cd "D:\\OntoChimpWeb\\tests"
conda activate env_python314
Execute: uvicorn main_min:app

"""
from fastapi import FastAPI

print(f"About to start FastAPI", flush=True) # what is flush?
app = FastAPI(
    title = "OntoChimpWeb",
    version="OCW_v0.1",
)

@app.get("/")
def root():
    return {
        "status": "OntoChimpWeb Online",
        "version": "0.1"
    }

@app.get("/ocw_version")
def show_version():
    return {
        "version": "OCW_v0.1"
    }
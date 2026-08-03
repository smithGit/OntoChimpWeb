"""
main.py for OntoChimpWeb - Initial FastAPI module for testing

2026-07-29 SMS Initial main.py for OntoChimpWeb
2026-08-03 SMS Adding logging

Folder: cd "D:\\OntoChimpWeb"
conda activate python314
Execute: uvicorn main:app

"""
from fastapi import FastAPI, HTTPException

from utils.mysql_select_columns import select_columns
# from fastapi.middleware.cors import CORSMiddleware


print(f"Starting OntoChimpWeb main.py — routes: /, /ocw_version, /select_term", 
      flush=True) # flush avoids buffering
app = FastAPI(
    title = "OntoChimpWeb",
    version="0.1",
)

@app.get("/")
def root():
    return {
        "status": "OntoChimpWeb Online",
        "version": "0.1 Diagnostic no routes...New Deployment"
    }

@app.get("/ocw_version")
def show_version():
    test_result = "No longeer doing: select_columns; do select_terms"
    return {
        "version": "OCW_v0.1",
        "module_test": test_result,
    }

@app.get("/select_terms")
def select_terms()->dict[str, object]:
    """
    return prototype terms stored in Azure MySQL
    """
    try:
        rows = select_columns(
            table_name="term_model_doc",
            column_names=[
                "term_id",
                "model_id",
                "doc_id",
                "term_norm",
            ],
        )
        return({
            "count":len(rows),
            "terms": rows
        })
    except Exception as exc:
        # Keep the detailed database error in Azure logs.
        print(f"/select_terms failed: {exc}", flush=True)

        # Do not send credentials or detailed infrastructure errors
        # to the browser.
        raise HTTPException(
            status_code=500,
            detail="Unable to retrieve terms from the database.",
        ) from exc


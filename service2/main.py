from typing import Optional

import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/success")
def success():
    return {"Message": "Hello World"}


@app.get("/warn")
def warn():
    raise HTTPException(status_code=404, detail="warn")


@app.get("/error")
def error():
    raise HTTPException(status_code=500, detail="error")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)

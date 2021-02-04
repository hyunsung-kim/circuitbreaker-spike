import logging
from typing import Optional

import uvicorn
from fastapi import FastAPI, HTTPException

from service import external_error_api
from service import external_success_api

app = FastAPI()
logger = logging.getLogger(__name__)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/cb-test/{call_num}")
def read_item(call_num: int):
    logger.info(f'call_num:{call_num}')
    if call_num > 0:
        external_success_api()
    else:
        try:
            external_error_api()
        except Exception as e:
            logger.exception(f'error circuitbreak test - {type(e)}')
            raise HTTPException(status_code=500, detail="warn")

    return {'cb-test': call_num}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

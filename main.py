import random
import string
import os

from fastapi import FastAPI, HTTPException
from starlette import status
from starlette.responses import Response

app = FastAPI(title="Debug app")
id = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(20))

@app.get("/app/get_id")
async def get_id():
    '''Get app id'''
    return {'id': id} #Response(status_code=status.HTTP_200_OK)


@app.get("/app/throw_exception")
async def throw_exception():
    '''Always app exit'''
    os._exit(1)


@app.get("/app/throw_exception/{app_id}")
async def throw_exception_arg(app_id):
    '''Selected app exit'''
    if id == app_id:
        await throw_exception()
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND)

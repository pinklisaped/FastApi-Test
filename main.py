import random
import string
import os
from typing import Optional

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
    '''Always app throw exception'''
    raise SystemExit('Some exception')


@app.get("/app/throw_exception/{app_id}")
async def throw_exception_arg(app_id):
    '''Selected app throw exception'''
    if id == app_id:
        await throw_exception()
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.get("/app/exit/{app_id}")
async def exit_app_id(app_id, exitcode: Optional[int] = 1):
    '''Selected app exit'''
    if id == app_id:
        await exit_app(exitcode)
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.get("/app/exit")
async def exit_app(exitcode: Optional[int] = 1):
    '''Always app exit'''
    os._exit(exitcode)

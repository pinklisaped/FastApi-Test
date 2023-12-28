import os
import platform
import random
import socket
import string
from typing import Optional

import psutil
from fastapi import FastAPI, HTTPException
from starlette import status
from starlette.responses import Response

app = FastAPI(title="Debug app")
id = ''.join(random.choice(string.ascii_lowercase +
             string.ascii_uppercase + string.digits) for i in range(20))


@app.get("/app/get_id")
async def get_id():
    '''Get app id'''
    return {'id': id}  # Response(status_code=status.HTTP_200_OK)


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


@app.get("/app/get_info")
async def get_info():
    '''Get info about OS'''
    uname = platform.uname()
    svmem = psutil.virtual_memory()
    architecture = platform.architecture()
    swap = psutil.swap_memory()
    cpufreq = psutil.cpu_freq()
    internal_ip = socket.gethostbyname(socket.gethostname())
    return {
        'Node': uname.node,
        'OS': f'{uname.system} {uname.release}',
        'Architecture': architecture[0],
        'Physical cores': psutil.cpu_count(logical=False),
        'Total cores': psutil.cpu_count(logical=True),
        'Frequency': cpufreq.max,
        'CPU model': platform.processor(),
        'RAM MB': int(svmem.total/1024/1024),
        'SWAP MB': int(swap.total/1024/1024),
        'IP address': internal_ip
    }

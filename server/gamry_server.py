# shell: uvicorn motion_server:app --reload
""" A FastAPI service definition for a potentiostat device server, e.g. Gamry.

The potentiostat service defines RESTful methods for sending commmands and retrieving 
data from a potentiostat driver class such as 'gamry_driver' or 'gamry_simulate' using
FastAPI. The methods provided by this service are not device-specific. Appropriate code
must be written in the driver class to ensure that the service methods are generic, i.e.
calls to 'poti.*' are not device-specific. Currently inherits configuration from driver 
code, and hard-coded to use 'gamry' class (see "__main__").
"""

import asyncio #ADDED
import time #ADDED

import os, sys

if __package__:
    # can import directly in package mode
    print("importing config vars from package path")
else:
    # interactive kernel mode requires path manipulation
    cwd = os.getcwd()
    pwd = os.path.dirname(cwd)
    print(pwd)
    if os.path.basename(pwd) == "helao-dev":
        sys.path.insert(0, pwd)
    if pwd in sys.path or os.path.basename(cwd) == "helao-dev":
        print("importing config vars from sys.path")
    else:
        raise ModuleNotFoundError("unable to find config vars, current working directory is {}".format(cwd))

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn
from pydantic import BaseModel
# from gamry_driver import *
from driver.gamry_simulate import *
from fastapi import Query
from typing import List
import asyncio
import json

app = FastAPI()


@app.on_event("startup")
def startup_event():
    global poti
    poti = gamry()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8003/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)


async def tester():
    while True:
        print("ah")
        await asyncio.sleep(1)

@app.websocket("/ws")
async def websocket_messages(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await poti.q.get()
        data = {k: [v] for k,v in zip(["t_s", "Ewe_V", "Ach_V", "I_A"], data)}
        await websocket.send_text(json.dumps(data))
        await websocket.send_text(json.dumps(porti.time_stamp))


class return_class(BaseModel):
    measurement_type: str
    parameters: dict
    data: list


@app.get("/potentiostat/get/potential_ramp")
async def pot_potential_ramp_wrap(
    Vinit: float, Vfinal: float, ScanRate: float, SampleRate: float
):
    value = await poti.potential_ramp(Vinit, Vfinal, ScanRate, SampleRate)
    return return_class(**value)


@app.get("/potentiostat/get/potential_cycle")
async def pot_potential_ramp_wrap(
    Vinit: float,
    Vfinal: float,
    Vapex1: float,
    Vapex2: float,
    ScanInit: float,
    ScanApex: float,
    ScanFinal: float,
    HoldTime0: float,
    HoldTime1: float,
    HoldTime2: float,
    Cycles: int,
    SampleRate: float,
    control_mode: str,
):
    return return_class(
        **poti.potential_cycle(
            Vinit,
            Vfinal,
            Vapex1,
            Vapex2,
            ScanInit,
            ScanApex,
            ScanFinal,
            HoldTime0,
            HoldTime1,
            HoldTime2,
            Cycles,
            SampleRate,
            control_mode,
        )
    )


# @app.get("/potentiostat/get/eis")
# async def eis_(start_freq: float, end_freq: float, points: int, pot_offset: float = 0):
#     return return_class(**poti.eis(start_freq, end_freq, points, pot_offset))


@app.get("/potentiostat/get/status")
async def status_wrapper():
    return return_class(
        measurement_type="status_query",
        parameters={"query": "potentiostat"},
        data=[await poti.status()],
    )


# @app.get("/potentiostat/get/signal_arr")
# async def signal_array_(Cycles: int, SampleRate: float, arr: str):
#     arr = [float(i) for i in arr.split(",")]
#     return return_class(**poti.signal_array(Cycles, SampleRate, arr))


@app.on_event("shutdown")
def shutdown_event():
    # this gets called when the server is shut down or reloaded to ensure a clean
    # disconnect ... just restart or terminate the server
    poti.close_connection()
    loop.close()
    return {"shutdown"}


if __name__ == "__main__":
    #poti = gamry()


    # loop = asyncio.get_event_loop() 
    # task1 = loop.create_task(poti.potential_ramp(-5, 5, 1, 0.1)) 
    # #task2 = loop.create_task(tester()) 
    # final_task = asyncio.gather(task1) 
    # loop.run_until_complete(final_task)

    # makes this runnable and debuggable in VScode
    # letters of the alphabet GAMRY => G6 A0 M12 R17 Y24
    uvicorn.run(app, host=FASTAPI_HOST, port=ECHEM_PORT)







    # http://127.0.0.1:8003/potentiostat/get/potential_ramp?Vinit=0&Vfinal=0.2&ScanRate=0.01&SampleRate=0.01

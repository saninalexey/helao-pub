import sys
sys.path.append(r'../config')
sys.path.append(r'../driver')
sys.path.append(r'../server')
import time
#from force import GSV3USB
#from force_driver import GSV3USB
# dev = GSV3USB(9)
#from mischbares_small import config
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import json
import requests
import os
from importlib import import_module
helao_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.join(helao_root, 'config'))
sys.path.append(os.path.join(helao_root, 'driver'))
#from force_driver import GSV3USB
config = import_module(sys.argv[1]).config
serverkey = sys.argv[2]
#dev = GSV3USB(9)

app = FastAPI(title="lang server V2", 
    description="This is a fancy lang motor action server", 
    version="2.0")


class return_class(BaseModel):
    parameters :dict = None
    data: dict = None


@app.get("/lang/getPos")
def getPos():
    res = requests.get("{}/langDriver/getPos".format(url)).json()
    retc = return_class(parameters= None, data=res)
    return retc

@app.get("/lang/moveRel")
def moveRelFar( dx: float, dy: float, dz: float):
    requests.get("{}/langDriver/moveRelFar".format(url), params= {"dx": dx, "dy": dy, "dz": dz}).json()
    retc = return_class(parameters= {"dx": dx, "dy": dy, "dz": dz,'units':{'dx':'mm','dy':'mm','dz':'mm'}},data=None)
    return retc

@app.get("/lang/moveDown") #24 is the maximum amount that it can gp down (24 - 2(initial) = 22)
def moveDown(dz: float,steps: float,maxForce: float, threshold:float=22.6):
    steps = int(steps)
    #threshold = 0.5
    force_value = []
    for i in range(steps):
        #uvicorn.run(app, host=config['servers'][serverkey]['host'], port=config['servers'][serverkey]['port'])
        #forceurl = "http://{}:{}".format(config['servers']['forceDriver']['host'], config['servers']['forceDriver']['port'])
        
        forceurl = config[serverkey]['forceurl']
        res = requests.get("{}/force/read".format(forceurl), params=None).json()
        #url = "http://{}:{}".format(config['servers']['force']['host'], config['servers']['force']['port'])
        #res = requests.get("{}/forceAction/read".format(url), params=None).json()
        force_value.append(res)
        print(res['data']['data']['value'])
        if dz > threshold:
            if abs(res['data']['data']['value']) > maxForce:
                print('Max force reached!')

            #requests.get("{}/lang/stopMove".format(url)).json()
            moveRelFar(dx= 0, dy=0, dz = threshold)
            print('axis are out of the range')

        else:
            if not abs(res['data']['data']['value'])> maxForce:
                print('Max force not reached ...')
                moveRelFar(dx= 0, dy=0, dz = dz)
            else:
                #requests.get("{}/lang/stopMove".format(url), params= None).json()
                print('Max force reached!')

        pos = getPos()
    retc = return_class(measurement_type='Move_relative', parameters= {"dz": dz,"steps":steps,"maxForce":maxForce},data={'pos':pos, 'force_value': force_value})
    return retc

@app.get("/lang/moveAbs")
def moveAbsFar(dx: float, dy: float, dz: float):
    print("the x and y position of the next point is {} and {}".format(dx, dy))
    print("types are {} and {}".format(type(dx), type(dy))) 
    requests.get("{}/langDriver/moveAbsFar".format(url), params= {"dx": dx, "dy": dy, "dz": dz}).json()
    retc = return_class(parameters= {"dx": dx, "dy": dy, "dz": dz,'units':{'dx':'mm','dy':'mm','dz':'mm'}},data=None)
    return retc

@app.get("/lang/moveHome")
def moveHome():
    res = requests.get("{}/langDriver/moveAbsFar".format(url), params=dict(dx=config[serverkey]['safe_home_pos'][0], dy=config[serverkey]['safe_home_pos'][1], dz=config[serverkey]['safe_home_pos'][2])).json()
    retc = return_class(parameters=None,data=res)
    return retc

@app.get("/lang/moveWaste")
def moveWaste(x: float=0, y: float=0, z: float=0): #these three coordinates define the home position. This helps us to align the positions based on the reference point 
    res = requests.get("{}/langDriver/moveAbsFar".format(url), params=dict(dx=x+config[serverkey]['safe_waste_pos'][0], dy=y+config[serverkey]['safe_waste_pos'][1], dz=z+config[serverkey]['safe_waste_pos'][2])).json()
    retc = return_class(parameters= {"x": x, "y": y, "z": z,'units':{'x':'mm','y':'mm','z':'mm'}},data=res)
    return retc

@app.get("/lang/moveSample")
def moveToSample(x: float=0, y: float=0, z: float=0):
    res = requests.get("{}/langDriver/moveAbsFar".format(url), params=dict(dx=x+config[serverkey]['safe_sample_pos'][0], dy=y+config[serverkey]['safe_sample_pos'][1], dz=z+config[serverkey]['safe_sample_pos'][2])).json()
    retc = return_class(parameters= {"x": x, "y": y, "z": z,'units':{'x':'mm','y':'mm','z':'mm'}},data=res)
    return retc

@app.get("/lang/RemoveDroplet")
def removeDrop(x: float=0, y: float=0, z: float=0):
    raw = []
    raw.append(requests.get("{}/langDriver/moveAbsFar".format(url), params= dict(dx = x + config[serverkey]['safe_waste_pos'][0], dy = y + config[serverkey]['safe_waste_pos'][1], dz = z + config[serverkey]['remove_drop'][2])).json()) # because referene will start from 2 
    raw.append(requests.get("{}/langDriver/moveAbsFar".format(url), params= dict(dx = x + config[serverkey]['remove_drop'][0], dy = y + config[serverkey]['remove_drop'][1], dz = z + config[serverkey]['remove_drop'][2])).json())
    res = requests.get("{}/langDriver/getPos".format(url)).json()
    raw.append(res)
    retc = return_class(parameters= {"x": x, "y": y, "z": z,'units':{'x':'mm','y':'mm','z':'mm'}},data={'raw':raw,'res':res['data']})
    return retc

@app.on_event("shutdown")
def shutDown():
    moveHome()


if __name__ == "__main__":

#    url = "http://{}:{}".format(config['servers']['lang']['host'], config['servers']['lang']['port'])
#    print('Port of lang Server: {}'.format(config['servers']['lang']['port']))
#    uvicorn.run(app, host=config['servers']['langDriver']['host'], port=config['servers']['langDriver']['port'])
    url = config[serverkey]['url']
    uvicorn.run(app, host=config['servers'][serverkey]['host'], 
                     port=config['servers'][serverkey]['port'])
    
    print("instantiated lang")
    
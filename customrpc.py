from pypresence import Presence
import json
import time

f = open('config.json')
config = json.load(f)
f.close()

clientid = config["clientid"]
details = config["details"]
state = config["state"]
largeimagekey = config["largeimagekey"]
largeimagetext = config["largeimagetext"]
smallimagekey = config["smallimagekey"]
smallimagetext = config["smallimagetext"]
partysize = config["partysize"]
partymax = config["partymax"]
starttime = config["starttime"]
endtime = config["endtime"]

partyinfo = [partysize, partymax]
if partysize is None or partymax is None:
    partyinfo = None

RPC = Presence(clientid)
RPC.connect()
RPC.update(details=details,state=state,large_image=largeimagekey,large_text=largeimagetext,small_image=smallimagekey,small_text=smallimagetext,party_size=partyinfo,start=starttime,end=endtime)

while True:
    time.sleep(3600)
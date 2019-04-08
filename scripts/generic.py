import os
import http.client
import ssl
import json

payload_file = os.environ['SERVICE']
with open(payload_file) as json_file:
    payload = json.load(json_file)

conn = http.client.HTTPSConnection("192.168.1.147:8443", context=ssl._create_unverified_context())

headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic YWRtaW46YWRtaW4=",
    'cache-control': "no-cache",
    }

conn.request("POST", url="/mgmt/shared/appsvcs/declare", body=json.dumps(payload), headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
'''
Created on Dec 16, 2014

@author: AlexFeng
'''
import sys
import json
import requests

my_headers = {'content-type': 'application/json-rpc'}
url = "http://10.75.53.21/ins"
username = "admin"
password = "cisco"


myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "sh version",
      "version": 1
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(username,password)).json()

print response

result = response['result']
kick_start_image = response['result']['body']['kickstart_ver_str']
host_name = response['result']['body']['host_name']

print ("")
print ("===============================")
print ('host name:'+ host_name)
print ('Image version :' + kick_start_image)
print ("===============================")

if __name__ == '__main__':
    pass

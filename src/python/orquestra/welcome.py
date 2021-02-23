"""
This module saves a welcome message.
"""

import json
import time
import os
import pwd
import subprocess

def welcome():
    message = "Hello World from Orquestra!"

    message_dict = {}
    message_dict["message"] = message
    message_dict["schema"] = "message"

    with open("welcome.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact
        print(os.environ)
        print("USER:" + pwd.getpwuid( os.getuid() )[ 0 ])
        subprocess.call(['pwd'])
#         subprocess.call(['cd', '/step/welcome-to-orquestra/src/python/orquestra'])
#         subprocess.call(['chmod','+x','./docker.sh'])
#         subprocess.call(['sh','./docker.sh'])
        #time.sleep(3600)
    for i in range(5):
        print("Gonna take a nap")
#         if i == 4:
#             raise ValueError('A very specific bad thing happened here. I like me some errors')
        
        time.sleep(2)
        

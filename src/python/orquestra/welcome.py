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
        #time.sleep(3600)
    for i in range(100):
        print(f"Break {i}")
        for j in range(100):
            time.sleep(10)
            print(f"From Break: {i} - Dancing: {j}")
            
    print('''
|-----------------------------------------------------------------------|
|    o   \ o /  _ o         __|    \ /     |__        o _  \ o /   o    |
|   /|\    |     /\   ___\o   \o    |    o/    o/__   /\     |    /|\   |
|   / \   / \   | \  /)  |    ( \  /o\  / )    |  (\  / |   / \   / \   |
|-----------------------------------------------------------------------|
        ''')
        

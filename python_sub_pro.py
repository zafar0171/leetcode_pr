#!/usr/bin/env python
#import time
import os
import subprocess

#subprocess.run(['date'])

#subprocess.run(['sleep', "2"])


#result = subprocess.run(['ls','This file does not exists'])
#print(result.returncode)


#Obtaining the output of a system command

# "host" exists on linux , not on windws

#result = subprocess.run(["nslookup", "8.8.8.8"], capture_output = True)
#print(result.returncode)
#print(result.stdout)
#print(result.stderr)



#Advanced subprocess management


my_env = os.environ.copy()

my_env["PATH"] = os.pathsep.join(["/my_app", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)

print(result)
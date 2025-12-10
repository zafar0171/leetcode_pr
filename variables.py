#!/usr/bin/env python 

import os


print("Home: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ''))
print("FRUIT: " + os.environ.get("FRUIT", ""))
print(os.environ.get("HOME"))
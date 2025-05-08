#!/usr/bin/env python3
# atrybut przechowuje envy 

# STAGE=staging ./os.py 
# STAGE=PROD ./os.py 

import os

stage = os.getenv("STAGE", default="DEV").upper()
output=f"We are running in:  {stage}"
if stage.startswith("PROD"):
    output="DANGER!!!" + output
print(output)

cwd = os.getcwd()
print(cwd)
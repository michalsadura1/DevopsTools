#!/usr/bin/env python3
# Create new user

import os, crypt

user= "testuser"
password = "Start@123"
encPass= crypt.crypt(password,"22")
os.system("useradd -p"+encPass+" "+ user)
print(f"User {user} created")
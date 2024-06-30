import getpass
import re
import json
import time
import multiprocessing
import threading

users_db = "users.json"

# kiểm tra tiêu chí mật khẩu tốt
def strong_password(password):
    if len(password) < 8:
        return False , "password has at least 8 character"
    if not re.search(r"[A-Z]", password):
        return False, "password has at least 1 uppercase character"
    if not re.search(r"[a-z]", password):
        return False, "password has at least 1 lowercase character"
    if not re.search(r"[0-9]", password):
        return False, "password has at least 1 number"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password ):
        return False, "pasword has at least 1 special character"
    return True, "This Strong Password"
print(strong_password("NguyenhanhNhan@2004"))


import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "24630538"))
    API_HASH = os.getenv("API_HASH", "f76710db60aba9fc37944efe3b2d20ae")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7281089138:AAGA77o0gKx_uY98d2BkcytvvSH83iQM8hE")
    sudo = os.getenv("SUDO")
    SUDO = [1753159645]
    if sudo:
        SUDO = make_int(sudo)

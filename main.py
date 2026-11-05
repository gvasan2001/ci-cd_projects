import data_base
import requests
import hashlib
import random
import json


aa=data_base.data_base()

def index():
    with open("/words.txt") as f:
        words = [w.strip() for w in f.readlines()]


    KEY = [hashlib.md5(i.encode()).digest() for i in words]
    aa.send_email("gokulavasan640@gmail.com", "start")


    for i in KEY:
        key_hex = i.hex()

        url = f"http://aes.cryptohack.org/passwords_as_keys/decrypt/c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66/{key_hex}/"

        try:
            response = requests.get(url, timeout=15)

            if response.status_code != 200:
                print("HTTP Error:", response.status_code)
                continue
            else:
                aa.send_email("gokulavasan640@gmail.com", "500")

            plaintext = response.json()

            hex_bytes = bytes.fromhex(plaintext["plaintext"])
            finalText = hex_bytes.decode("utf-8", errors="replace")
            print(finalText)

            if finalText.startswith("crypto"):
                aa.send_email("gokulavasan640@gmail.com", finalText)

        except (requests.RequestException, ValueError, KeyError) as e:
            print("Error:", e)
            continue


index()

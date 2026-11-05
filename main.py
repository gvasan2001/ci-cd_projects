
import data_base
import requests
import hashlib
import random
import json


aa=data_base.data_base()

def index():
    with open("words.txt") as f:
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
                
                # Create a detailed error message string
                error_details = (
                    f"CryptoHack Request Failed!\n\n"
                    f"Status Code: {response.status_code}\n"
                    f"Attempted URL: {url}\n"
                    f"Response Body: {response.text}\n"
                )
                
                # Send the detailed message instead of just "500"
                aa.send_email("gokulavasan640@gmail.com", error_details)
                continue
        
        
            plaintext = response.json()
        
            hex_bytes = bytes.fromhex(plaintext["plaintext"])
            finalText = hex_bytes.decode("utf-8", errors="replace")
            print(finalText)
        
            if finalText.startswith("crypto"):
                aa.send_email("gokulavasan640@gmail.com", finalText)
        
        except requests.exceptions.RequestException as e:
                    # This catches network drops, DNS failures, or connection timeouts
                    network_error_details = f"Network Connection Failed!\n\nException details: {str(e)}"
                    aa.send_email("gokulavasan640@gmail.com", network_error_details)


index()

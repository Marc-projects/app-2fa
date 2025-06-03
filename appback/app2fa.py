import requests
import time, sys


TOKEN_MARC = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiTWFyYyJ9.UBc7UkdPck3QiocTszzdQzT76-yjzFkC6dcCgIVAZxs"
TOKEN_MAILYS = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiTWFpbHlzIn0.YCxopzr2DSmuFE8IvJNZOjiMN5_x_M8ul1mtjhpL5xY"
API_2FA = "https://marc-projects-2fa/api"


r = requests.get(API_2FA, headers = {"Authorization": TOKEN_MARC}, verify='ac.pem')
res = r.json()
timestamp = int(time.time())
cycle = 30 - (timestamp - res['lastChange'])

while cycle >= 0:
    if cycle == 0:
        r = requests.get(API_2FA, headers = {"Authorization": TOKEN_MARC}, verify='ac.pem')
        res = r.json()
        timestamp = int(time.time())
        cycle = 30 - (timestamp - res['lastChange'])
        sys.stdout.write(f"\rMot de passe temporaire : {res['tempPass']}, temps restant : {cycle} secondes")
    else:
        time.sleep(1)
        cycle -= 1
        sys.stdout.write(f"\rMot de passe temporaire : {res['tempPass']}, temps restant : {cycle} secondes")

from urllib.request import Request, urlopen
from hashlib import sha256
import json 

def Latest_Round():

     req= Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'})
     data = json.loads(urlopen(req).read().decode())
     latest_Round = int(str(data["round"]))
     
     return latest_Round




def Range_Of_Rounds(latestRound):
    
    first_Round = latestRound - 100 
    randomness_array = []

    for roundNumber in range(first_Round, latestRound + 1):
        req = Request('https://drand.cloudflare.com/public/' + str(roundNumber), headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'})
        data = json.loads(urlopen(req).read().decode())

        randomness_array.append((data["randomness"]))

    return randomness_array


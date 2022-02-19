from urllib.request import Request, urlopen
from binascii import unhexlify, hexlify
import json


def max(binaryRandomness):
    maxOnes = max(map(len, binaryRandomness.split('0')))
    maxZeros = max(map(len, binaryRandomness.split('1')))

    return maxOnes, maxZeros


def hexToBinary(hexRandomness):

    result = bin(int(hexRandomness, 16))

    return result[2:]


def mergeRandomn(randomnessArray):

    mergedRandomn = bytes()
    for randomness in randomnessArray:
        randomness = unhexlify(randomness)
        mergedRandomn += randomness

    return hexlify(mergedRandomn)


def Latest(): #Let's Find the latest round 

    req = Request(' https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36'})
    data = json.loads(urlopen(req).read().decode())
    latestRound = int(str(data["round"]))

    return latestRound


def Range(latestRound): #Trying to find the range of the rounds 
    firstRound = latestRound - 99
    randomn_array = []

    for roundNumber in range(firstRound, latestRound + 1):
        req = Request('https://drand.cloudflare.com/public/' + str(roundNumber), headers={
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36'})
        data = json.loads(urlopen(req).read().decode())

        randomn_array.append(data["randomness"])

    return randomn_array


def main():
    latestRound = Latest()
    rangeOfRoundsArray = Range(latestRound)
    mergedRandomn = mergeRandomn(rangeOfRoundsArray).decode()
    binaryRandomness = hexToBinary(mergedRandomn)

    maxOnes, maxZeros = max(binaryRandomness)
    
    print("Largest sequence of 0s: ", maxZeros) #length of the biggest sequences
    print("--------------")
    print("Largest sequence of 1s: ", maxOnes)
    
    


if __name__ == "__main__":
    main()

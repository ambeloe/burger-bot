import csv
import time
import secrets
import requests

header = {
    'Content-type': 'application/json'
}

webhook_url = "YOUR WEBHOOK URL GOES HERE"

pogdict = {
    "content": "burger gif",
    "embeds": [{
        "image": {
            "url": "https://i.imgur.com/Z546MhC.gif"
        }
    }]
}

def inform():
    burger = parseCSV("mentions.csv")
    gifs = parseCSV("burger-gifs.csv")
    if getting.random() < 0.25:
        pogdict["content"] = "<@&" + secrets.choice(burger[0]) + "> burger gif"
    else:
        pogdict["content"] = "burger gif"
    pogdict["embeds"][0]["image"]["url"] = secrets.choice(gifs)[0]
    requests.post(webhook_url, json=pogdict, headers=header)
    pass

def parseCSV(filename):
    with open(filename, newline='') as f:
        return list(csv.reader(f, skipinitialspace=True))


getting = secrets.SystemRandom()

while True:
    inform()
    time.sleep(secrets.randbelow(3600))

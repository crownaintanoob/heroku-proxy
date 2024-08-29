import os
import requests
from lxml import html

from flask import request
from flask import Flask
from flask import Response


app = Flask(__name__)


@app.route('/')
def home():
    usage = 'erm what the sigma!'
    return usage

@app.route('/inventorygetplr/<userid>/<cursor>')
def root(userid, cursor):
    cursorString = "&cursor=" + cursor if len(cursor) >= 1 else '&cursor=""'
    url = "https://www.roblox.com/users/inventory/list-json?assetTypeId=34" + cursorString + "&itemsPerPage=50&pageNumber=1&userId=" + userid
    r = requests.get(url, proxies={
        "http": os.environ.get("httpProxyUrl"),
        "https":  os.environ.get("httpsProxyUrl")
    })
    rr = Response(response=r.content, status=r.status_code)
    rr.headers["Content-Type"] = r.headers['Content-Type']
    return rr

@app.route('/passesgetfromgame/<gameid>/<cursor>')
def root2(gameid, cursor):
    dataUniverseId = requests.get("https://apis.roblox.com/universes/v1/places/" + gameid + "/universe", proxies={
        "http": os.environ.get("httpProxyUrl"),
        "https":  os.environ.get("httpsProxyUrl")
    })
    datajsonGot = dataUniverseId.json()
    cursorString = "&cursor=" + cursor if len(cursor) >= 1 else '&cursor=""'
    url = "https://games.roblox.com/v1/games/3803580056/game-passes?limit=30&sortOrder=Asc?cursor=213424"
    print(datajsonGot)
    print(f'{datajsonGot["universeId"]}')
   # url = "https://games.roblox.com/v1/games/" + f'{datajsonGot["universeId"]}' + "/game-passes?limit=15&sortOrder=Asc" + cursorString
    r = requests.get(url, proxies={
        "http": os.environ.get("httpProxyUrl"),
        "https":  os.environ.get("httpsProxyUrl")
    })
    rr = Response(response=r.content, status=r.status_code)
    rr.headers["Content-Type"] = r.headers['Content-Type']
    return rr

@app.route('/listgames/<userid>')
def root3(userid):
    url = "https://games.roblox.com/v2/users/" + userid + "/games?accessFilter=public&sortOrder=Asc&limit=25"
    r = requests.get(url, proxies={
        "http": os.environ.get("httpProxyUrl"),
        "https":  os.environ.get("httpsProxyUrl")
    })
    rr = Response(response=r.content, status=r.status_code)
    rr.headers["Content-Type"] = r.headers['Content-Type']
    return rr


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 8000.
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)

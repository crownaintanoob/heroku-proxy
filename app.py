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
    url = "https://www.roblox.com/users/inventory/list-json?assetTypeId=34" + cursorString + "&itemsPerPage=100&pageNumber=1&userId=" + userid
    r = requests.get(url, proxies={
        "http": "http://qywiproxy-rotate:qywiErmWhatTheSigma6959@p.webshare.io:80/",
        "https": "http://qywiproxy-rotate:qywiErmWhatTheSigma6959@p.webshare.io:80/"
    })
    rr = Response(response=r.content, status=r.status_code)
    rr.headers["Content-Type"] = r.headers['Content-Type']
    return rr

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 8000.
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)

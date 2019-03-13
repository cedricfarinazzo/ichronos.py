import requests
import os, tempfile
from utils import *

def schedule_request(url, ext=".ics", verbose=False, cache=True):
    url = url + ext
    urlf = url.replace("https", "").replace("http", "").replace("://", "").replace("/", "_")
    filecache = os.path.join(tempfile.gettempdir(), urlf)
    
    if cache:
        data = readCache(filecache, verbose=verbose)
        if data is not None:
            return data
            
    if verbose:
        print("[+] url: " + url)
    tstart = time.time()
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("Failed to establish a new connection: [Errno 11001] getaddrinfo failed")
        return None
    if verbose:
        print("[+] Get page in " + ("%.3f" % (time.time() - tstart))	+ " seconds")
        print("[+] Header: ")
        for key, value in r.headers.items():
            print("[+]     %s: %s" % (key, value))
        print("[+]     %s: %d o" % ("Raw size", len(r.content)))
        print("[+] status_code: " + str(r.status_code))
    if r.text != "" and r.status_code == 200:
        if cache:
            writeCache(filecache, r.text, verbose=verbose)
        return r.text
    return None

import os
import time
import datetime

def inCache(file, verbose=False, expire=3600*24):
    if os.path.exists(file):
        lastupdate_file = os.path.getctime(file)
        difftime = time.time() - lastupdate_file
        return difftime < expire
    return False
    
def readCache(file, verbose=False, expire=3600*24):
    if not inCache(file, verbose=verbose, expire=expire):
        return None
    try:
        with open(file, 'r') as f:
            text = f.read()
        if text != "":
            if verbose:
                print("[+] cache file: " + file)
        return text
    except IOError:
        if verbose:
            print("[+] Cannot read cache")
    return None
        
def writeCache(file, data, verbose=False):
    try:
        if os.path.exists(file):
            os.remove(file)
    except:
        pass
    try:
        with open(file, 'w') as f:
            f.write(data)
        if verbose:
            print("[+] cache file created: " + file)
        return True
    except IOError:
        if verbose:
            print("[+] Cannot write file")
        return False

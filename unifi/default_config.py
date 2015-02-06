from __future__ import print_function
import os,sys
import simplejson

def load_config():
    try:
        f = open(os.path.expanduser('~/.unifi.json'),'r')
        cnts = f.read().strip()
        f.close()
        settings = simplejson.loads(cnts)
        return settings
    except Exception, e:
        print("Could not load settings %s" % e) 
        sys.exit() 
    


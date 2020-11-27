#!/usr/bin/python3 -W ignore::DeprecationWarning

import requests
import json
import sys
import time
import ipaddress
import apifunctions
import cgi,cgitb

#remove the InsecureRequestWarning messages
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

"""
Greg_Dunlap / CelticCow
"""

def search4grp(mds, cma, eai):
    debug = 1
    endl = "\n"
    print("in search4grp")

    user     = "roapi"
    password = "1qazxsw2"

    sid = apifunctions.login(user, password, mds, cma)

    if(debug == 1):
        print("session id : " + sid, end=endl)
    




    ##don't need publish
    time.sleep(5)
    logout_result = apifunctions.api_call(mds, "logout", {}, sid)
    if(debug == 1):
        print(logout_result, end=endl)
#end of search4grp

def main():
    debug = 1
    endl = "\n"

    print("in main", end=endl)


    mds      = "146.18.96.16"
    cma      = "146.18.96.25"
    

    eai = "123456"

    search4grp(mds, cma, eai)

if __name__ == "__main__":
    main()
#end of program
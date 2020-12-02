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
    debug = 0
    endl = "<br>"
    if(debug == 1):
        print("in search4grp")

    user     = "roapi"
    password = "1qazxsw2"

    sid = apifunctions.login(user, password, mds, cma)

    if(debug == 1):
        print("session id : " + sid, end=endl)
    
    check_name = {
        "order" : [
            {
                "ASC" : "name"
            }
        ],
        "type" : "group",
        "in" : ["name", eai]
    }

    name_result = apifunctions.api_call(mds, "show-objects", check_name, sid)

    if(debug == 1):
        print("-------------------------------------------")
        print(name_result, end=endl)

        print(name_result['total'], end=endl)
    
    for i in range(name_result['total']):
        print("Group Found : ", end="")
        print(name_result['objects'][i]['name'], end=endl)

        show_group_json = {"name" : name_result['objects'][i]['name']}

        group_contents = apifunctions.api_call(mds, "show-group", show_group_json, sid)

        if(debug == 1):
            print("*************************************", end=endl)
            print(group_contents, end=endl)

        print("contents of group: ", end=endl)
        for j in range(len(group_contents['members'])):
            print(group_contents['members'][j]['name'], end=" ")
            print(group_contents['members'][j]['type'], end=endl)

    ##don't need publish
    time.sleep(5)
    logout_result = apifunctions.api_call(mds, "logout", {}, sid)
    if(debug == 1):
        print(logout_result, end=endl)
#end of search4grp

def main():
    debug = 1
    endl = "<br>"

    form = cgi.FieldStorage()

    eai = form.getvalue('eai2search')

    mds      = "146.18.96.16"
    cma      = "146.18.96.25"
    

    #eai = "123456"

    ## html header and config data dump
    print ("Content-type:text/html\r\n\r\n")
    print ("<html>")
    print ("<head>")
    print ("<title>EAI Search Results</title>")
    print ("</head>")
    print ("<body>")
    print("EAI Search results<br><br>")

    search4grp(mds, cma, eai)

    print("------- end of program -------", end=endl)
    print("<br><br>")
    print("</body>")
    print("</html>")



if __name__ == "__main__":
    main()
#end of program
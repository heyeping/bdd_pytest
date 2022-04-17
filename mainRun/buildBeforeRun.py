# coding:utf-8
# @Time   :2022/1/5 16:22
# @Author :Nicholas.liu
# @File   :buildBeforeRun.py
# @Software   :bdd_test

import requests
from requests.auth import HTTPBasicAuth
import json
from ayla_public.public import get_pathfile
import os
def get_Main_command(project):
    if project == "zhijia" :
        jql='''project = YW AND status = "In QA" AND "is_auto[Dropdown]" = Y order by updated DESC'''

    url = "https://aylaasia.atlassian.net/rest/api/3/search"

    auth = HTTPBasicAuth("nicholas.liu@aylaasia.com", "BFO12LAFHfj5F1dRmXyiFC6C")

    headers = {
          "Accept": "application/json",
       "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "expand": [
        "names",
        ],

      "jql": jql,
      "fieldsByKeys": False,
      "fields": [
          "key"
      ],
      "startAt": 0
    } )

    response = requests.request(
       "POST",
       url,
       data=payload,
       headers=headers,
       auth=auth
    )


    message=json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    messagedic=json.loads(message)


    cardlist=[]
    for i in messagedic["issues"]:
        cardlist.append(i["key"])

    print(cardlist)

    #start to match testCases
    testCasePath=os.path.join(get_pathfile(), "testSteps")
    # print(testCasePath)
    fileNamelist=os.listdir((testCasePath))

    command=""
    commandlist=[]
    for j in fileNamelist:
        for k in cardlist:
            if j.count(k) >0:
                # command="\"../testSteps/"+j+"\""+","
                command = "../testSteps/" + j
                commandlist.append(command)


    # print("command[:-1]",command[:-1])
    # return command[:-1]
    print(commandlist)
    return  commandlist






# get_Main_command("zhijia")
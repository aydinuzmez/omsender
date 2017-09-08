# -*- coding: utf-8 -*-
# Copyright (c) 2017-2018, Aydin Uzmez
#
# This module is part of quickConvert and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause
#   File
#    - Author: Aydin Uzmez
#    - File : fusion
#    - Date: Sep 2017


import json
import urllib2
import os
import fusion

IP = "http://192.168.0.3:14125/api/"
API_KEY = "3DHS33113425CEEX0HXS7FQ3X77S3457"
#ROOM = os.environ["COMPUTERNAME"]+"1231"
USER = os.environ["USERNAME"]
MESSAGECOLOR = "#F7CA18"
#TRANSFER = "SERKANA"
TRANSFER = "AYDINU"


class Message(object):
    def __init__(self):
        self.data = {
            #"ROOM": ROOM,
            "from":USER,
            "to":TRANSFER,
            "color":MESSAGECOLOR,
            "notify":1,
            "message": "",
        }
        self.data2 = {
            #"ROOM": ROOM,
            "from":TRANSFER,
            "to":USER,
            "color":MESSAGECOLOR,
            "notify":1,
            "message": "",
        }

        self.url_chat = IP+r"/notify"
        self.req = urllib2.Request(self.url_chat)

        self.req.add_header('Accept', "application/json, text/javascript, */*")
        self.req.add_header("API-KEY", API_KEY)

    def write(self, write):
        self.data["message"] = write
        self.data2["message"] = write
        response = urllib2.urlopen(self.req, json.dumps(self.data))
        response2 = urllib2.urlopen(self.req, json.dumps(self.data2))
        json_response= json.load(response)
        json_response2= json.load(response2)
        print TRANSFER + " Message Sent: " + str(json_response["success"])
        print USER + " Message Sent: " + str(json_response2["success"])
        return json_response["success"]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True

try:
    message1 = Message()
    saver1 = fusion.Saver()
    path = saver1.get_filename()[1]
    print "Saver's path: " + path
    if path is not None:
        message1.write(path)

except urllib2.HTTPError,e:
    print (e.code,e.msg)

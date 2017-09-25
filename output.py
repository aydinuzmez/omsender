# -*- coding: utf-8 -*-
# Copyright (c) 2017-2018, Aydin Uzmez
#
# This module is part of quickSender and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause
#   File
#    - Author: Aydin Uzmez
#    - File : fusion
#    - Date: Sep 2017

DEBUG = 0

import json
import urllib2
import os
import logging
import time


IP = "http://192.168.0.3:14125/api/"
API_KEY = "3DHS33113425CEEX0HXS7FQ3X77S3457"
#ROOM = os.environ["COMPUTERNAME"]+"1231"
USER = os.environ["USERNAME"]
MESSAGECOLOR = "#F7CA18"

if DEBUG == 0:
    TRANSFER = "SERKANA"
else:
    TRANSFER = "AYDINU"

current_folder = os.path.dirname(__file__)
log_path = os.path.join(current_folder, "log", time.strftime("%d_%m_%Y")+".log")


logging.basicConfig(
    filename=log_path,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt="%I:%M:%S %p"
                    )


class Message(object):
    def __init__(self,write):
        self.__to_transfer = {
            "from":USER,
            "to":TRANSFER,
            "notify":1,
            "message": "",
        }
        self.__to_user = {
            "from":TRANSFER,
            "to":USER,
            "color": MESSAGECOLOR,
            "notify":1,
            "message": "",
        }
            #"ROOM": ROOM,
        self.url_chat = IP+r"/notify"
        self.write = write

    def request(self):
        req = urllib2.Request(url=self.url_chat)
        req.add_header('Accept', "application/json, text/javascript, */*")
        req.add_header("API-KEY", API_KEY)
        return req

    def to_user(self):
        try:
            self.__to_user["message"] = self.write
            response = urllib2.urlopen(self.request(), data=json.dumps(self.__to_user))
            json_response = json.load(response)

            print "User {0} sent message, Result: ".format(USER) + str(json_response["success"])
        except urllib2.HTTPError, e:
            print (e.code, e.msg)

    def to_transfer(self):
        try:
            self.__to_transfer["message"] = self.write
            response = urllib2.urlopen(self.request(), data=json.dumps(self.__to_transfer))
            json_response = json.load(response)

            print "Transfer {0} sent message, Result: ".format(TRANSFER) + str(json_response["success"])
            logging.info("log: %s ", {"user":USER,
                                       "status":str(json_response["success"]),
                                        "path":self.write}
                         )
        except urllib2.HTTPError, e:
            print (e.code, e.msg)
            logging.warning("log: %s", {"code": e.code,"msg": e.msg})

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True

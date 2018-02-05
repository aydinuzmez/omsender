# -*- coding: utf-8 -*-
# Copyright (c) 2017-2018, Aydin Uzmez
#
# This module is part of quickSender and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause
#   File
#    - Author: Aydin Uzmez
#    - File : lib
#    - Date: Sep 2017

import json
import config
import urllib2
import os
import time
import logging

if config.DEBUG != 0: config.TRANSFER = config.USER

log_path = os.path.join(os.path.dirname(__file__), "log", time.strftime("%d_%m_%Y")+".log")

logging.basicConfig(
    filename=log_path,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt="%I:%M:%S %p"
                    )

class Message(object):
    def __init__(self,write=""):
        self.__to_transfer = {
            "from":config.USER,
            "to":config.TRANSFER,
            "notify":1,
            "message": "",
        }
        self.__to_user = {
            "from":config.TRANSFER,
            "to":config.USER,
            "color": config.MESSAGECOLOR,
            "notify":1,
            "message": "",
        }
        self.url_chat = config.IP+r"/notify"
        self.write = write

    def setWrite(self,write_param):
        self.write = write_param

    def request(self):
        req = urllib2.Request(url=self.url_chat)
        req.add_header('Accept', "application/json, text/javascript, */*")
        req.add_header("API-KEY", config.API_KEY)
        return req

    def to_user(self):
        try:
            self.__to_user["message"] = self.write
            response = urllib2.urlopen(self.request(), data=json.dumps(self.__to_user))
            json_response = json.load(response)

            print "User {0} sent message, Result: ".format(config.USER) + str(json_response["success"])
        except urllib2.HTTPError, e:
            print (e.code, e.msg)
        except TypeError, e:
            print "ss"

    def to_transfer(self):
        try:
            self.__to_transfer["message"] = self.write
            print self.__to_transfer
            response = urllib2.urlopen(self.request(), data=json.dumps(self.__to_transfer))
            json_response = json.load(response)
            
            print "Transfer {0} sent message, Result: ".format(config.TRANSFER) + str(json_response["success"])
            logging.info("log: %s ", {"user":config.USER,
                                       "status":str(json_response["success"]),
                                        "path":self.write}
                         )
        except (urllib2.HTTPError, urllib2.URLError), e:
            print e
            logging.warning("log: %s", {"user": config.USER,"msg": e})

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True

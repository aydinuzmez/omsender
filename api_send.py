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
ROOM = os.environ["COMPUTERNAME"]+"1231"
USER = os.environ["USERNAME"]
MESSAGECOLOR = "#F7CA18"
#TRANSFER = "SERKANA"
TRANSFER = "BURAKK"

class Room(object):
    def __init__(self):
        self.__chat_json = {
            "roomname": ROOM,
            "roomusers": USER+"|0,"+TRANSFER+"|0",
        }
        self.__response =self.get()

    def __get_url(self, url):
        """
        ip is adding
        :param url:
        :return:
        """
        added_url = IP + url
        return added_url

    def __url_req(self, url):
        """
        return req
        :param url:
        :return:
        """
        req = urllib2.Request(self.__get_url(url))
        req.add_header('Accept', "application/json, text/javascript, */*")
        req.add_header("API-KEY", API_KEY)
        return req

    def get(self):
        """
        Boolean: True or False
        :return:
        """
        self.req = self.__url_req("chatrooms/" + ROOM)
        response = urllib2.urlopen(self.req)
        json_response = json.load(response)
        return json_response

    def is_there_room(self):
        return self.__response["success"]

    def create(self):
        if self.is_there_room() is False:
            create_req = self.__url_req("chatrooms")
            response = urllib2.urlopen(create_req, json.dumps(self.__chat_json))
            json_response = json.load(response)
            if json_response["success"] is True:
                print ROOM + "that new chat ROOM created"
                return json_response["success"]
            else:
                print "json_response: {0} - {1} didn't create ".format(json_response,ROOM)
                return False

        else:
            print ROOM+ " already has "

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True


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
    #ROOM = "COMP-9"
    chat1 = Room()
    message1 = Message()
    saver1 = fusion.Saver()
    path = saver1.get_filename()[1]
    print "Saver's path: " + path
    if path is not None:
        if chat1.is_there_room() is True:
            message1.write(path)
        else:
            print ROOM + " didn't found"
            chat1.create()  #BURASI KALKACAK OZEL MESAJ CALISTIGI ICIN
            message1.write(path)

except urllib2.HTTPError,e:
    print (e.code,e.msg)

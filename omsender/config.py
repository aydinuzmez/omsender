# -*- coding: utf-8 -*-
# Copyright (c) 2017-2018, Aydin Uzmez
#
# This module is part of quickConvert and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause
#   File
#    - Author: Aydin Uzmez
#    - File : config
#    - Date: Sep 2017

import os

"""
transfer e filepath mi gönderilsin. dirpath mi gonderilsin.
api-key buraya gelecek
"""


def setup():
    DEBUG = 1
    TRANSFER = "AYDINU"
    IP = "http://192.168.0.3:14125/api/"
    API_KEY = "3DHS33113425CEEX0HXS7FQ3X77S3457"
    USER = os.environ["USERNAME"]
    MESSAGECOLOR = "#F7CA18"

def fusion():
    COMP_PATHMAP = "Project:"
    PATH_PATHMAP = "Project"


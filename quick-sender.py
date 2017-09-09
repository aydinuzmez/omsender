# -*- coding: utf-8 -*-
# Copyright (c) 2017-2018, Aydin Uzmez
#
# This module is part of quickConvert and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause
#   File
#    - Author: Aydin Uzmez
#    - File : quick-sender
#    - Date: Sep 2017

from output import Message
from fusion import Saver
import urllib2


def run():
    try:
        message1 = Message()
        saver1 = Saver()
        if saver1.is_saver():
            if saver1.is_there_clip():
                path = saver1.get_filename()[1]
                message1.write(path)
                print "Project's Path:  " + path
            else:
                print "#Info: There isn't any project's path in the node"
        else:
            print "#Info: This is no The Saver or The Loader"

    except urllib2.HTTPError,e:
        print (e.code,e.msg)


if __name__ == '__main__':
    run()
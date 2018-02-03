# -*- coding: utf-8 -*-
# Copyright (c) 2017-2018, Aydin Uzmez
#
# This module is part of quickSender and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause
#   File
#    - Author: Aydin Uzmez
#    - File : quick-sender
#    - Date: Sep 2017

from output import Message
from fusion import Saver

def run():
    saver1 = Saver()
    path = saver1.get_filename()
    if path is not None:
        message1 = Message(path)
        message1.to_transfer()
        message1.to_user()
        print "Project's Path:  " + path

if __name__ == '__main__':
    run()
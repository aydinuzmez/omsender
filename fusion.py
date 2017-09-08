# -*- coding: utf-8 -*-
# Copyright (c) 2017-2018, Aydin Uzmez
#
# This module is part of quickConvert and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause
#   File
#    - Author: Aydin Uzmez
#    - File : fusion
#    - Date: Sep 2017

import PeyeonScript

"""
fusion = eyeon.scriptapp("Fusion")
comp = fusion.GetCurrentComp()
comp_active_tool = comp.ActiveTool

if comp_active_tool is not None:
    if comp_active_tool.ID == "Saver":
        print comp_active_tool.ID
        if comp_active_tool.GetInput("Clip"):
            print comp_active_tool.GetInput("Clip")
        else:
            print None
    else:
        print None
"""

#fusion = PeyeonScript.scriptapp("Fusion")

COMPPATHMAP = "Project:"
FILEPATHMAP = "Project"


"""
@@@@@@@@@@@@@ATTENTION@@@@@@@@


__bos saver geldigin hata veriyor.
__baska bir node secili ikende veriyor sikicemmm

"""


class Saver(object):
    def __init__(self):
        self.fusion = PeyeonScript.scriptapp("Fusion")
        self.comp = self.fusion.GetCurrentComp()
        self.comp_active_tool = self.comp.ActiveTool

    def __saver_control(self):
        if self.comp_active_tool is not None:
            if self.comp_active_tool.ID == "Saver":
                return True
            else:
                return False
        else:
            return False

    def __get_pathmap(self):
        pathmap_response = self.comp.GetCompPathMap(False, False)
        if pathmap_response[COMPPATHMAP]:
            #print "Pathmap_response: ",pathmap_response[COMPPATHMAP]
            return pathmap_response[COMPPATHMAP]
        else:
            return None

    def __path_split(self):
        response= str(self.comp_active_tool.GetInput("Clip"))
        return response.split(":")

    def __from_project_to_path(self):
        """
        pdivide
        :return: 
        """
        filename_split = self.__path_split()
        project_pathmap = self.__get_pathmap()

        if filename_split[0] == FILEPATHMAP:
            return "Path",project_pathmap+filename_split[1]
        else:
            print "Return None, fusion.py>__from_project_to_path"
            return None

    def get_filename(self):
        if self.__saver_control() is True:

            if self.__get_pathmap() is None:
                print self.comp_active_tool.GetInput("Clip")
                return self.comp_active_tool.GetInput("Clip")
            else:
                #print self.__from_project_to_path()
                return self.__from_project_to_path()
        else:
            print "This is not the Saver.","Result:",None
            return None

if __name__ == '__main__':
    saver1 = Saver()
    saver1.get_filename()
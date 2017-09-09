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
import re

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

COMP_PATHMAP = "Project:"
PATH_PATHMAP = "Project"


"""
@@@@@@@@@@@@@ATTENTION@@@@@@@@


__bos saver geldigin hata veriyor. [TAMAM]
__baska bir node secili ikende veriyor [TAMAM]

__  - "project:" Pathmap var ama
    -  saver'da "project:" yok

"""


class Saver(object):
    def __init__(self):
        self.fusion = PeyeonScript.scriptapp("Fusion")
        self.comp = self.fusion.GetCurrentComp()
        self.comp_active_tool = self.comp.ActiveTool
        self.path = str(self.comp_active_tool.GetInput("Clip"))


    def is_saver(self):
        if self.comp_active_tool is not None:
            if self.comp_active_tool.ID == "Saver" or self.comp_active_tool.ID == "Loader":
                return True
            else:
                return False
        else:
            return False

    def is_there_clip(self):
        if self.comp_active_tool.GetInput("Clip"):
            return True
        else:
            return False

    def __get_pathmap(self):
        pathmap_response = self.comp.GetCompPathMap(False, False)
        if pathmap_response[COMP_PATHMAP]:
            #print "Pathmap_response: ",pathmap_response[COMP_PATHMAP]
            return pathmap_response[COMP_PATHMAP]
        else:
            return None

    def __path_split(self):
        return self.path.split(":")

    def __path_match(self):
        """
        :return: 
        """
        nesne = re.match(PATH_PATHMAP,self.path)
        if nesne:
            return True
        else:
            return False,"__path_match False"

    def __get_path(self):
        pass

    def __from_project_to_path(self):
        path_split = self.__path_split()
        project_pathmap = self.__get_pathmap()

        if path_split[0] == PATH_PATHMAP:
            return project_pathmap+path_split[1]
        else:
            print "Return None, fusion.py>__from_project_to_path"
            return None

    def get_filename(self):
        """
        
        :return: 
        """
        if self.is_saver() is True:
            prefix = "Path"
            if self.__get_pathmap() is None:
                return prefix,self.comp_active_tool.GetInput("Clip")
            else:
                """
                - "project:" Pathmap var ama
                -  saver'da "project:" yok
                :return: 
                """
                if self.__path_match() is True:
                    return prefix, self.__from_project_to_path()
                else:
                    return prefix, self.comp_active_tool.GetInput("Clip")
        else:
            print "This isn't the Saver.","Result:", None
            return None

if __name__ == '__main__':
    saver1 = Saver()
    saver1.get_filename()
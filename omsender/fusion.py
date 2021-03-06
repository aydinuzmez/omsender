# -*- coding: utf-8 -*-
# Copyright (c) 2017-2018, Aydin Uzmez
#
# This module is part of quickSender and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause
#   File
#    - Author: Aydin Uzmez
#    - File : fusion
#    - Date: Sep 2017

import PeyeonScript
import re
import os
import config

class Saver(object):
    def __init__(self):
        self.fusion = PeyeonScript.scriptapp("Fusion")
        self.comp = self.fusion.GetCurrentComp()
        self.comp_active_tool = self.comp.ActiveTool
        if self.comp_active_tool is not None:
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
        if pathmap_response:
            #print "Pathmap_response: ",pathmap_response[COMP_PATHMAP]
            return pathmap_response[config.COMP_PATHMAP]
        else:
            return None

    def __path_split(self):
        return self.path.split(":")

    def __path_match(self):
        """
        :return: 
        """
        nesne = re.match(config.PATH_PATHMAP,self.path)
        if nesne:
            return True
        else:
            return False,"__path_match False"

    def __get_path(self):
        pass

    def __from_project_to_path(self):
        path_split = self.__path_split()
        project_pathmap = self.__get_pathmap()
        if path_split[0] == config.PATH_PATHMAP:
            #path_split[1].encode("string-escape")
            match = re.match(os.sep.encode("string-escape"), path_split[1])
            if match:
                path_split[1] = path_split[1].lstrip("\\")
                return os.path.join(project_pathmap, path_split[1])
            else:
                return os.path.join(project_pathmap, path_split[1])
        else:
            print "Return None, fusion.py>__from_project_to_path"
            return None

    def __isfile(self, filepath):
        return os.path.isfile(filepath)

    def __dir_name(self, path=None):
        if path is None:
            filename = self.comp_active_tool.GetInput("Clip")
        else:
            filename = path
            print filename
            print self.__isfile(filename)
        if self.__isfile(filename) is True:
            return os.path.dirname(filename)
        else:
            print "Path taken isn't file"
            return None

    def get_filename(self):
        if self.is_saver() is True:
            if self.is_there_clip():
                if self.__get_pathmap() is None:
                    return self.__dir_name()
                else:
                    """
                    - "project:" Pathmap var ama
                    -  saver'da "project:" yok
                    :return:
                    """
                    if self.__path_match() is True:
                        path = self.__from_project_to_path()
                        return self.__dir_name(path)
                    else:
                        return self.__dir_name()
            else:
                print "There isn't any project's path in the node"
                return None
        else:
            print "This is no The Saver or The Loader"
            return None

if __name__ == '__main__':
    saver1 = Saver()
    saver1.get_filename()
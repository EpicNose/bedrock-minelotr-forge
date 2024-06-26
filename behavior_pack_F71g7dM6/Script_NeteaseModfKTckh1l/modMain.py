# -*- coding: utf-8 -*-

from mod.common.mod import Mod


@Mod.Binding(name="Script_NeteaseModfKTckh1l", version="0.0.1")
class Script_NeteaseModfKTckh1l(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseModfKTckh1lServerInit(self):
        pass

    @Mod.DestroyServer()
    def Script_NeteaseModfKTckh1lServerDestroy(self):
        pass

    @Mod.InitClient()
    def Script_NeteaseModfKTckh1lClientInit(self):
        pass

    @Mod.DestroyClient()
    def Script_NeteaseModfKTckh1lClientDestroy(self):
        pass

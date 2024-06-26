# -*- coding: utf-8 -*-

from mod.common.mod import Mod
from mod_log import logger
import mod.server.extraServerApi as serverApi



@Mod.Binding(name="Script_NeteaseModfKTckh1l", version="0.0.1")
class Script_NeteaseModfKTckh1l(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseModfKTckh1lServerInit(self):
        # print('hello')
        # serverApi.RegisterSystem("DemoTutorialMod", "Server","Script_DemoTutorialMod.DemoTutorialServerSystem.DemoTutorialServerSystem")
        serverApi.RegisterSystem("Script_NeteaseModfKTckh1l","Server","Script_NeteaseModfKTckh1l.NeteaseServerSystem.NeteaseServerSystem")
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

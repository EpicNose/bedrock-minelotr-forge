# -*- coding: utf-8 -*-

from mod.common.mod import Mod
from mod_log import logger
import mod.server.extraServerApi as serverApi
import config


@Mod.Binding(name="config.mod_name", version="0.0.1")
class MineLOTRmod(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def MineLOTRServerInit(self):
        # print('hello')
        # serverApi.RegisterSystem("DemoTutorialMod", "Server","Script_DemoTutorialMod.DemoTutorialServerSystem.DemoTutorialServerSystem")
        # serverApi.RegisterSystem("MineLOTR","Server","Script_MineLOTR.MineLOTRServerSystem.MineLOTRServerSystem")
        serverApi.RegisterSystem(config.mod_name, config.server_system_name, config.server_class_path)
        pass

    @Mod.DestroyServer()
    def MineLOTRServerDestroy(self):
        pass

    @Mod.InitClient()
    def MineLOTRClientInit(self):
        pass

    @Mod.DestroyClient()
    def MineLOTRClientDestroy(self):
        pass

# -*- coding: utf-8 -*-

from mod.common.mod import Mod
from mod_log import logger
import mod.server.extraServerApi as serverApi
import mod.client.extraClientApi as clientApi
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
        print "111111111111111111111111111111111111111111111111111111111111"
        pass

    @Mod.DestroyServer()
    def MineLOTRServerDestroy(self):
        pass

    @Mod.InitClient()
    def MineLOTRClientInit(self):
        clientApi.RegisterSystem(config.mod_name, config.client_system_name, config.client_class_path)
        print "222222222222222222222222222222222222222222222222222222222222"
        pass

    @Mod.DestroyClient()
    def MineLOTRClientDestroy(self):
        pass

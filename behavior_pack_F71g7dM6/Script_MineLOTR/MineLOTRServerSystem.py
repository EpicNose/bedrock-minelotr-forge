# -*- coding: utf-8 -*-
from mod_log import logger
import Preset.Controller.PresetApi as presetApi
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()



class MineLOTRServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        # self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ActorHurtServerEvent",self, self.OnActorHurtServer)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "PlayerDoInteractServerEvent",self, self.OnOpenForgeUI)

    # OnScriptTickServer的回调函数，会在引擎tick的时候调用，1秒30帧（被调用30次）
    def OnTickServer(self):
        """
        Driven by event, One tick way
        """


        pass

    # 这个Update函数是基类的方法，同样会在引擎tick的时候被调用，1秒30帧（被调用30次）
    def Update(self):
        """
        Driven by system manager, Two tick way
        """
        # print(1)
        pass

    def Destroy(self):
        pass

    # def OnActorHurtServer(self, args):
    #     comp = serverApi.GetEngineCompFactory().CreateAction(args["entityId"])
    #     comp.SetMobKnockback(0.1, 0.1, 10.0, 1.0, 1.0)
    #     # serverApi.GetEngineCompFactory().

    def OnOpenForgeUI(self,args):
        print "尝试输出参数"
        print args
        # playercomp = serverApi.GetEngineCompFactory().
        entity = serverApi.GetEngineCompFactory().CreateEntityComponent(args["interactEntityId"])
        comp = serverApi.GetEngineCompFactory().CreateEntityDefinitions(args["interactEntityId"])
        result = comp.GetEntityDefinitions()
        print result
        if result.__contains__("+minelotr:entity"):
            print "命中"


        # player = serverApi.GetEngineCompFactory().CreatePlayer(args["playerId"])
        # print player.GetPlayerHunger()
        # print entity.GetAllComponentsName()
        # entity.
        # obj = presetApi.GetGameObjectByEntityId(args["playerId"])
        # print obj

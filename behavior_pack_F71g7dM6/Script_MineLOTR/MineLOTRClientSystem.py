# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
import config

class MineLOTRClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'UiInitFinished', self, self.onForgeUIreg)
        # 注册与铁匠交互的来自于服务端的事件
        self.ListenForEvent('MineLOTR', 'MineLOTRServer', 'PlayerInteractWithCraftsman', self,self.PlayerInteractWithCraftsman)

        print "监听UI初始化结束事件"
    # 监听引擎OnScriptTickClient事件，引擎会执行该tick回调，1秒钟30帧
    def OnTickClient(self):
        """
        Driven by event, One tick way
        """
        pass

    # 被引擎直接执行的父类的重写函数，引擎会执行该Update回调，1秒钟30帧
    def Update(self):
        """
        Driven by system manager, Two tick way
        """
        pass

    def Destroy(self):
        pass

    def onForgeUIreg(self,data):
        # 注册自定义箱子的屏幕为脚本内的UI，第一个参数是注册为的UI的命名空间，第二个参数为注册为的UI的键名，即标识符，第三个参数为代理类所在路径，第四个参数为JSON UI中屏幕控件名
        clientApi.RegisterUI('ui_minelotr_forge1', 'minelotr_forge', 'Script_MineLOTR.uiScript.ForgeUIScreenNode.ForgeUIScreenNode','ui_minelotr_forge1.main')
        print "注册执行完成注册执行完成注册执行完成注册执行完成注册执行完成注册执行完成注册执行完成注册执行完成注册执行完成"

    def PlayerInteractWithCraftsman(self,data):

        print "客户端已收到"
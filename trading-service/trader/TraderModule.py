from trader.core.constants.Constants import ConfigConstants
from trader.data.DataServer import DataServer
from trader.data.api.ServiceApi import TraderServiceApi
from trader.data.module.DataServiceModule import TraderServiceModule
from trader.data.source.cache.ServiceCache import TraderServiceDataCache, AccountCache, UserCache, PositionsCache
from trader.gateway.service.GatewayService import GatewayService
from trader.gateway.service.GatewayServiceModule import GatewayServiceModule
from trader.gateway.service.api.GatewayServiceApi import GatewayServiceApi
from trader.gateway.socket.WebSocketConnectionManager import WebSocketConnectionManager
from trader.gateway.socket.WebSocketConnectionSource import WebSocketConnectionSource
from trader.core.config.ConfigUtil import ConfigUtils


class TraderModule:



    def start(self):
        host: str = ConfigUtils.getConfigs().get(ConfigConstants.WebSocketServerSection).get(
            ConfigConstants.ServerHostKey)
        port: int = int(ConfigUtils.getConfigs().get(ConfigConstants.WebSocketServerSection).get(
            ConfigConstants.ServerPortKey))
        connectionManager: WebSocketConnectionManager = WebSocketConnectionManager()
        ws: WebSocketConnectionSource = WebSocketConnectionSource(
            host=host, port=port, connectionManager=connectionManager)

        gsm: GatewayServiceModule = GatewayServiceModule(connectionManager=connectionManager)
        GatewayServiceApi.gatewayServiceModule = gsm
        gs: GatewayService = GatewayService(gatewayServiceModule=gsm)

        # data service
        dataSourceManager: TraderServiceDataCache = TraderServiceDataCache(
            accountsCache=AccountCache(), userCache=UserCache(), positionsCache=PositionsCache())
        dsm: TraderServiceModule = TraderServiceModule(dataSourceManager=dataSourceManager)
        TraderServiceApi.traderServiceModule = dsm
        ds: DataServer = DataServer(dsm)

        #
        ds.start()
        gs.start()
        ws.start()

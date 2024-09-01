from trader.gateway.module.IGateway import IGateway
from trader.gateway.module.WebSocketGateway import WebSocketGateway
import logging

from trader.gateway.service.GatewayService import GatewayService
from trader.gateway.service.GatewayServiceModule import GatewayServiceModule


class Gateway:
    Logger = logging.getLogger(__name__)

    @staticmethod
    def initializeGatewayService(gw: IGateway):
        gsm: GatewayServiceModule = GatewayServiceModule(connectionManager=gw.getConnectionManager())
        gs: GatewayService = GatewayService(gatewayServiceModule=gsm)
        gs.start()

    if __name__ == "main":
        Logger.info("Starting Gateway")
        gw: IGateway = WebSocketGateway()
        initializeGatewayService(gw)
        gw.start()

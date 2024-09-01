import os
from trader.core.constants.Constants import ConfigConstants
from trader.gateway.service.GatewayServiceModule import GatewayServiceModule
from trader.gateway.service.api.GatewayServiceApi import GatewayServiceApi
from trader.core.config.ConfigUtil import ConfigUtils
from trader.core.thread.StoppableThread import StoppableThread
import logging


class GatewayService:
    _logger = logging.getLogger(__name__)
    _server: StoppableThread = None
    _gatewayServiceModule: GatewayServiceModule = None

    def __init__(self, gatewayServiceModule: GatewayServiceModule):
        self._gatewayServiceModule = gatewayServiceModule

    @staticmethod
    def handleStartServer():
        host = ConfigUtils.getConfig(ConfigConstants.GatewayServerSection, ConfigConstants.GatewayServerHost)
        port = ConfigUtils.getConfig(ConfigConstants.GatewayServerSection, ConfigConstants.GatewayServerPort)
        server = ConfigUtils.getConfig(ConfigConstants.GatewayServerSection, ConfigConstants.GatewayServerWindows)
        if os.name == "nt":
            server = ConfigUtils.getConfig(ConfigConstants.GatewayServerSection, ConfigConstants.GatewayServerWindows)

        GatewayServiceApi.gatewayServiceApi.run(
            host=host,
            port=int(port),
            server=server,
            debug=True
        )

    def start(self):
        self._server = StoppableThread(name="GatewayService", target=GatewayService.handleStartServer)
        self._server.start()

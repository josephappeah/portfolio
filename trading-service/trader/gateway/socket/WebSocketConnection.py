import asyncio
import logging
from abc import ABC
from websockets import WebSocketServerProtocol

from trader.core.constants.Constants import ConfigConstants
from trader.core.model.Data import Message
from trader.gateway.model.IConnection import IConnection
from trader.gateway.model.IDataDestination import IDataDestination
from trader.gateway.model.IDataSource import IDataSource
from trader.gateway.socket.WebSocketDataDestination import WebSocketDataDestination
from trader.gateway.socket.WebSocketDataSource import WebSocketDataSource
from trader.core.config.ConfigUtil import ConfigUtils


class WebSocketConnection(IConnection, ABC):
    Logger = logging.getLogger(__name__)
    _webSocket: WebSocketServerProtocol = None
    _dataSource: IDataSource = None  # in coming messages to send to client
    _dataDestination: IDataDestination = None  # out going messages coming from client

    def __init__(self, webSocket: WebSocketServerProtocol):
        self._dataDestination, self._dataSource = WebSocketDataDestination(), WebSocketDataSource()
        super().__init__(self._dataSource, self._dataDestination)
        self._webSocket = webSocket
        webSocket.ping_timeout = int(ConfigUtils.getConfig(ConfigConstants.WebSocketsSection,
                                                           ConfigConstants.WebSocketConnectionTimeout))

    async def open(self):
        async def connectionHandlerLoop():
            while True:
                if self._dataSource.hasMessages():
                    outGoingMessage: Message = self._dataSource.getMessageQueue().popleft()
                    await self._webSocket.send(outGoingMessage.getQuote().toString())
                # inComingMessage: Optional[Any] = await self._webSocket.recv()
                # if inComingMessage:
                #     message: Message = Message(inComingMessage)
                #     self._onMessage(message)

        def connectionHandlerLoopAsyncRunner():
            asyncio.run(connectionHandlerLoop())

        await asyncio.to_thread(connectionHandlerLoopAsyncRunner)

    def close(self):
        self._webSocket.close()

    def _onMessage(self, message: Message) -> None:
        self._dataDestination.consume(message)

    def isOpen(self) -> bool:
        return self._webSocket.open

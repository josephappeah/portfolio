import asyncio
from websockets import WebSocketServerProtocol, serve
from trader.gateway.model.IConnectionManager import IConnectionManager
from trader.gateway.model.IConnectionSource import IConnectionSource
from trader.gateway.socket.WebSocketConnection import WebSocketConnection
from trader.core.thread.StoppableThread import StoppableThread


class WebSocketConnectionSource(IConnectionSource):
    _server: StoppableThread = None
    _host: str = None
    _port: int = None
    _name: str = None

    def __init__(self, host: str, port: int, connectionManager: IConnectionManager):
        super().__init__(connectionManager)
        self._host, self._port = host, port
        self._name = self.getName()

    def start(self):
        # TODO: Start this on the self._server thread
        asyncio.run(self._handleStart())

    def stop(self):
        self._server.stop()

    async def _handleConnection(self, websocket: WebSocketServerProtocol):
        if websocket:
            connection: WebSocketConnection = WebSocketConnection(websocket)
            connection.setConnectionKey(websocket.origin)
            connectionName: str = self._connectionManager.addConnection(connection)
            connection.setConnectionName(connectionName)
            await connection.open()

    def getName(self) -> str:
        if not self._name:
            self._name = (self._host + ":" + str(self._port)).upper()
        return self._name

    async def _handleStart(self):
        async with serve(self._handleConnection, self._host, self._port):
            await asyncio.Future()  # run forever

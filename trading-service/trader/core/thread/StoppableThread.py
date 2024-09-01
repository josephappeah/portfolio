from threading import Thread
from typing import Any, Coroutine
import logging
from trader.core.thread.ThreadUtil import ThreadUtils


class StoppableThread:
    Logger = logging.getLogger(__name__)

    _name: str = None
    _target: Any = None
    _thread: Thread | Coroutine = None
    _shouldStop: bool = False

    def __init__(self, name, target):
        self._name, self._target = name, target

    def start(self):
        self.Logger.info("Starting Thread: {%s}", self._name)
        self._thread = ThreadUtils.createNewDaemonThread(target=self._target, stop=self._handleStop)

    async def startAsync(self):
        self.Logger.info("Starting Async Thread: {%s}", self._name)
        self._thread = await ThreadUtils.createNewDaemonThreadAsync(target=self._target, stop=self._handleStop)

    def stop(self):
        self.Logger.debug("Stopping Thread: {%s}", self._name)
        self._shouldStop = True

    def _handleStop(self):
        return self._shouldStop

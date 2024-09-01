from threading import Thread
from typing import Optional, Any

import asyncio


class ThreadUtils:

    @staticmethod
    def createNewDaemonThread(target: Optional[Any], stop: Any) -> Thread:
        thread: Thread = Thread(target=ThreadUtils.indefiniteLoop, args=(target, stop))
        thread.daemon = True
        thread.start()
        return thread

    @staticmethod
    async def createNewDaemonThreadAsync(target: Optional[Any], stop: Any) -> Thread:

        def s():
            loop = asyncio.new_event_loop()
            # asyncio.set_event_loop(loop)
            loop.run_until_complete(ThreadUtils.indefiniteLoopAsync(target, stop))
            loop.run_forever()

        thread: Thread = Thread(target=s)
        thread.daemon = True
        thread.start()
        return thread

    @staticmethod
    def indefiniteLoop(target: Optional[Any], stop: Any):
        if target:
            while True:
                target()
                if stop():
                    break

    @staticmethod
    async def indefiniteLoopAsync(target: Optional[Any], stop: Any):
        if target:
            while True:
                await target()
                if stop():
                    break

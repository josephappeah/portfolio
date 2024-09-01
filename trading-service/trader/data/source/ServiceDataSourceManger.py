from typing import List

from trader.core.model.Data import Position, AccountBalance


class TraderServiceDataSourceManager:
    def getPositionsForUser(self) -> List[Position]:
        pass

    def addPositionForUser(self):
        pass

    def getAccountBalanceForUser(self) -> List[AccountBalance]:
        pass

    def updateAccountBalanceForUser(self):
        pass


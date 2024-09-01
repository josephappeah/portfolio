from typing import List

from trader.core.model.Data import AccountBalance, User, Position


class AccountCache:
    _userNameToAccountBalance: dict[str:dict[str:AccountBalance]] = None

    def __init__(self):
        self._userNameToAccountBalance = {}

    def removeUser(self, user: User):
        if user.getUsername() in self._userNameToAccountBalance:
            del self._userNameToAccountBalance[user.getUsername()]

    def addAccountForUser(self, user: User, account: AccountBalance):
        userAccounts: dict[str:AccountBalance] = self._userNameToAccountBalance.get(user.getUsername(), {})
        userAccounts[account.getCurrency()] = account
        self._userNameToAccountBalance[user.getUsername()] = userAccounts

    def getAccountsForUser(self, user: User) -> List[AccountBalance]:
        userAccounts: dict[str:AccountBalance] = self._userNameToAccountBalance.get(user.getUsername(), {})
        return list(userAccounts.values()) if userAccounts else []


class UserCache:
    _userCache: dict[str:User] = None

    def __init__(self):
        self._userCache = {}

    def addUser(self, user: User):
        self._userCache[user.getUsername()] = user

    def removeUser(self, user: User):
        if user.getUsername() in self._userCache:
            del self._userCache[user.getUsername()]


class PositionsCache:
    _userNameToPositionsCache: dict[str:List[Position]] = None

    def __init__(self):
        self._userNameToPositionsCache = {}

    def removeUser(self, user: User):
        if user.getUsername() in self._userNameToPositionsCache:
            del self._userNameToPositionsCache[user.getUsername()]

    def removePositionForUser(self, user: User, position: Position):
        pass

    def addPositionForUser(self, user: User, position: Position):
        userPositions: List[Position] = self._userNameToPositionsCache.get(user.getUsername(), [])
        userPositions.append(position)
        print(position.toString())
        self._userNameToPositionsCache[user.getUsername()] = userPositions

    def getPositionsForUser(self, user: User):
        return self._userNameToPositionsCache.get(user.getUsername(), [])


class TraderServiceDataCache:
    _accountsCache: AccountCache = None
    _positionsCache: PositionsCache = None
    _userCache: UserCache = None

    def __init__(self, accountsCache: AccountCache, positionsCache: PositionsCache, userCache: UserCache):
        self._positionsCache, self._accountsCache = positionsCache, accountsCache
        self._userCache = userCache

    # Users
    def addUser(self, user: User):
        if self._userCache:
            self._userCache.addUser(user)

    def removeUser(self, user: User):
        if self._userCache:
            self._userCache.removeUser(user)
        if self._positionsCache:
            self._positionsCache.removeUser(user)

    # Positions
    def addPositionForUser(self, user: User, position: Position):
        if self._positionsCache:
            self._positionsCache.addPositionForUser(user, position)
        else:
            print("no cache")

    def removePositionForUser(self, user: User, position: Position):
        if self._positionsCache:
            self._positionsCache.removePositionForUser(user, position)

    def getPositionsForUser(self, user: User) -> List[Position]:
        if self._positionsCache:
            return self._positionsCache.getPositionsForUser(user)

    # Accounts
    def addAccountForUser(self, user: User, account: AccountBalance):
        if self._accountsCache:
            self._accountsCache.addAccountForUser(user, account)

    # def removeAccountForUser(self, user: User, account: AccountBalance):
    #     if self._accountsCache:
    #         self._accountsCache.(user, account)

    def getAccountsForUser(self, user: User) -> List[AccountBalance]:
        if self._accountsCache:
            return self._accountsCache.getAccountsForUser(user)

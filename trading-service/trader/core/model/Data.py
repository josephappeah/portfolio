"""
    {
        account: {
            accountId: "",
            accountBalance: []
        },
        messageType: MessageType.Undefined,
        positions: [],
        quote: {
            assetName: "",
            quote: ""
        },
        user: {
            origin: "",
            username: ""
        }
    }
"""
from typing import List


class Quote:
    _assetName: str = None
    _quote: str = None

    def __init__(self, assetName: str = None, quote: str = None):
        self._quote, self._assetName = quote, assetName

    def fromJson(self, quoteJson: dict):
        if "assetName" in quoteJson:
            self._assetName = quoteJson["assetName"]

        if "quote" in quoteJson:
            self._quote = quoteJson["quote"]

    def toJson(self) -> dict:
        return {
            "assetName": self._assetName,
            "quote": self._quote
        }

    def toString(self) -> str:
        return str(self.toJson())

    def getQuote(self) -> str:
        return self._quote

    def getAssetName(self) -> str:
        return self._assetName


class Position:
    _id: str = None
    _amount: int = None
    _status: str = None
    _side: str = None
    _assetName: str = None
    _quote: Quote = None

    def __init__(self,
                 amount: int = None,
                 status: str = None,
                 side: str = None,
                 assetName: str = None,
                 id: str = None,
                 quote: Quote = None
                 ):
        self._amount, self._side = amount, side
        self._assetName, self._status = assetName, status
        self._id, self._quote = id, quote

    def fromJson(self, positionJson: dict):
        if "side" in positionJson:
            self._side = positionJson["side"]

        if "assetName" in positionJson:
            self._assetName = positionJson["assetName"]

        if "side" in positionJson:
            self._amount = positionJson["amount"]

        if "status" in positionJson:
            self._status = positionJson["status"]

    def toJson(self) -> dict:
        return {
            "assetName": self._assetName,
            "side": self._side,
            "amount": self._amount,
            "status": self._status,
            "id": self._id,
            "quote": self._quote.toString()
        }

    def toString(self) -> str:
        return str(self.toJson())

    def getAssetName(self) -> str:
        return self._assetName

    def getAmount(self) -> int:
        return self._amount

    def getSide(self) -> str:
        return self._side

    def getStatus(self) -> str:
        return self._status

    def setStatus(self, status):
        self._status = status

    def getId(self) -> str:
        return self._id

    def getQuote(self) -> Quote:
        return self._quote


class AccountBalance:
    _balance: int = None
    _currency: str = None

    def __init__(self, balance: int = None, currency: str = None):
        self._currency, self._balance = currency, balance

    def fromJson(self, accountBalanceJson: dict):
        if "balance" in accountBalanceJson:
            self._balance = accountBalanceJson["balance"]

        if "currency" in accountBalanceJson:
            self._currency = accountBalanceJson["currency"]

    def toJson(self) -> dict:
        return {
            "balance": self._balance,
            "currency": self._currency
        }

    def toString(self) -> str:
        return str(self.toJson())

    def getCurrency(self) -> str:
        return self._currency

    def getBalance(self) -> int:
        return self._balance


class Account:
    _accountId: str = None
    _accountBalance: List[AccountBalance] = None

    def __init__(self, accountId: str = None, accountBalance: List[AccountBalance] = None):
        self._accountBalance, self._accountId = accountBalance, accountId

    def _parseAccountBalance(self, accountBalances: List[dict]) -> List[AccountBalance]:
        parsedAccountBalances: List[AccountBalance] = []
        for accountBalance in accountBalances:
            parsedAccountBalance = AccountBalance()
            parsedAccountBalance.fromJson(accountBalance)
            parsedAccountBalances.append(parsedAccountBalance)
        return parsedAccountBalances

    def fromJson(self, accountBalanceJson: dict):
        if "accountId" in accountBalanceJson:
            self._accountId = accountBalanceJson["accountId"]

        if "accountBalance" in accountBalanceJson:
            self._accountBalance = self._parseAccountBalance(accountBalanceJson["accountBalance"])

    def toJson(self):
        return {
            "accountId": self._accountId,
            "accountBalance": [accountBalance.toJson() for accountBalance in self._accountBalance] if
            self._accountBalance else []
        }

    def toString(self) -> str:
        return str(self.toJson())

    def getAccountBalance(self) -> List[AccountBalance]:
        return self._accountBalance

    def getAccountId(self) -> str:
        return self._accountId


class User:
    _username: str = None
    _origin: str = None

    def __init__(self, username: str = None, origin: str = None):
        self._origin, self._username = origin, username

    def fromJson(self, userJson: dict):
        if "username" in userJson:
            self._username = userJson["username"]

        if "origin" in userJson:
            self._origin = userJson["origin"]

    def toJson(self) -> dict:
        return {
            "origin": self._origin,
            "username": self._username
        }

    def toString(self) -> str:
        return str(self.toJson())

    def getOrigin(self) -> str:
        return self._origin

    def getUsername(self) -> str:
        return self._username


class Message:
    _messageType: str = None
    _quote: Quote = None
    _account: Account = None
    _positions: List[Position] = None
    _user: User = None

    def __init__(self, quote=None, messageType=None, user=None, account=None, positions=None):
        self._quote, self._messageType = quote, messageType
        self._user, self._account = user, account
        self._positions = positions

    def fromJson(self, messageJson: dict):
        if "messageType" in messageJson:
            self._messageType = messageJson["messageType"]

        if "quote" in messageJson:
            self._quote = messageJson["quote"]

        if "account" in messageJson:
            self._account = messageJson["account"]

        if "user" in messageJson:
            self._user = messageJson["user"]

        if "positions" in messageJson:
            self._positions = messageJson["positions"]

    def toJson(self) -> dict:
        return {
            "account": self._account.toString() if self._account else {},
            "messageType": self._messageType if self._messageType else "",
            "positions": [position.toString() for position in self._positions] if self._positions else [],
            "user": self._user.toString() if self._user else {},
            "quote": self._quote.toString() if self._quote else {}
        }

    def toString(self) -> str:
        return str(self.toJson())

    def setQuote(self, quote: Quote):
        self._quote = quote

    def getMessageType(self) -> str:
        return self._messageType

    def getQuote(self) -> Quote:
        return self._quote

    def getPositions(self) -> List[Position]:
        return self._positions

    def getUser(self) -> User:
        return self._user

    def getAccount(self) -> Account:
        return self._account

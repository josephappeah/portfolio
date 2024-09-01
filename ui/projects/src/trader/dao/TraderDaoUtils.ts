import {TraderConfig} from "../configs/configs";
import {AccountBalance} from "../model/Account";
import {Position} from "../model/Position";
import {Message, MessageType} from "../model/Message";
import {Quote} from "../model/Quote";

export class TraderDaoUtils {

    public static getTraderService(): string {
        return TraderConfig.TraderService.quoteService.Host +
            TraderConfig.TraderService.quoteService.Port
    }

    public static getDataService(): string {
        return TraderConfig.TraderService.dataService.Host +
            TraderConfig.TraderService.dataService.Port
    }

    public static getRFQRequestPath(): string {
        return TraderDaoUtils.getTraderService() + TraderConfig.TraderService.paths.RFQ
    }

    public static getNewPositionRequestPath(): string {
        return TraderDaoUtils.getDataService() + TraderConfig.TraderService.paths.NewPosition
    }

    public static getNewPositionRequestParams(quote: Quote, position: Position): Message {
        return {
            messageType: MessageType.NewPosition,
            account: {
                accountId: window.origin,
                accountBalance: []
            },
            positions: [position],
            quote: quote,
            user: {
                origin: window.origin,
                username: window.origin
            }
        }
    }

    public static getRFQRequestParams(assetName: string): Message {
        return {
            messageType: MessageType.RequestForQuote,
            account: {
                accountId: window.origin,
                accountBalance: []
            },
            positions: [],
            quote: {
                assetName: assetName,
                quote: ""
            },
            user: {
                origin: window.origin,
                username: window.origin
            }
        }
    }

    public static getUpdateAccountBalanceRequestPath(): string {
        return TraderDaoUtils.getDataService() + TraderConfig.TraderService.paths.UpdateAccountBalance
    }

    public static getUpdateAccountBalanceRequestParams(accountBalance: AccountBalance[]): Message {
        return {
            messageType: MessageType.AccountBalanceUpdate,
            account: {
                accountId: window.origin,
                accountBalance: accountBalance
            },
            positions: [],
            quote: {
                assetName: "",
                quote: ""
            },
            user: {
                origin: window.origin,
                username: window.origin
            }
        }
    }

    public static getFetchAccountBalanceRequestParams(accountBalance: AccountBalance[]): Message {
        return {
            messageType: MessageType.RequestAccountBalance,
            account: {
                accountId: window.origin,
                accountBalance: accountBalance
            },
            positions: [],
            quote: {
                assetName: "",
                quote: ""
            },
            user: {
                origin: window.origin,
                username: window.origin
            }
        }
    }

    public static getFetchPositionsRequestParams(): Message {
        return {
            messageType: MessageType.RequestPosition,
            account: {
                accountId: window.origin,
                accountBalance: []
            },
            positions: [],
            quote: {
                assetName: "",
                quote: ""
            },
            user: {
                origin: window.origin,
                username: window.origin
            }
        }
    }

    public static getPositionsRequestPath(): string {
        return TraderDaoUtils.getDataService() + TraderConfig.TraderService.paths.GetPositions
    }

    public static parsePositions(data: any): Position[] {
        const parsedPositions: Position[] = []
        for (let position of data.data.response) {
            parsedPositions.push(JSON.parse(JSON.stringify(position)) as unknown as Position)
        }
        return parsedPositions
    }

    public static getAccountBalanceRequestPath(): string {
        return TraderDaoUtils.getDataService() + TraderConfig.TraderService.paths.GetAccountBalance
    }

    public static parseAccountBalance(data: any): AccountBalance[] {
        const parsedBalance: AccountBalance[] = []
        for (let accountBalance of data.data.response) {
            parsedBalance.push(JSON.parse(JSON.stringify(accountBalance)) as unknown as AccountBalance)
        }
        return parsedBalance
    }
}
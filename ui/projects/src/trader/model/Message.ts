import {Quote} from "./Quote";
import {Account, AccountBalance, DefaultAccountBalance} from "./Account";
import {Position} from "./Position";

export enum MessageType {
    Undefined = "Undefined",
    RequestForQuote = "RequestForQuote",
    AccountBalanceUpdate = "AccountBalanceUpdate",
    RequestAccountBalance = "RequestAccountBalance",
    RequestPosition = "RequestPosition",
    NewPosition = "NewPosition",
}

export type Message = {
    messageType: MessageType;
    quote: Quote;
    account: Account;
    positions: Position[];
    user: User;
}

export type User = {
    origin: string;
    username: string;
}

export const DefaultMessage: Message = {
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

export class MessageUtils {

    public static newMessage(): Message {
        return DefaultMessage;
    }

    public static newAccount(): Account {
        return DefaultAccountBalance
    }

    public static createAccount(accountId: string, accountBalance: AccountBalance[]): Account {
        return {
            accountId: accountId,
            accountBalance: accountBalance
        }
    }

    public static setMessageType(message: Message, messageType: MessageType) {
        message.messageType = messageType;
        return message;
    }

    public static setAccount(message: Message, account: Account): Message {
        message.account = account;
        return message;
    }
}
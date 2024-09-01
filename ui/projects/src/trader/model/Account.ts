export enum Currency {
    USD = "USD",
    EUR = "EUR",
    GBP = "GBP",
    JPY = "JPY",
}

export const CurrencyToCurrencySymbolMap = {
    "USD" : "$",
    "EUR" : "€",
    "GBP" : "£",
    "JPY" : "¥"
}

export type AccountBalance = {
    balance: number;
    currency: Currency;
}

export type Account = {
    accountId: string;
    accountBalance: AccountBalance[];
}

export const DefaultAccountBalance: Account = {accountBalance: [
        {
            balance: 500000,
            currency: Currency.USD,
        },
        {
            balance: 500000,
            currency: Currency.EUR,
        },
        {
            balance: 500000,
            currency: Currency.JPY,
        },
        {
            balance: 500000,
            currency: Currency.GBP,
        },
    ], accountId: window.origin}
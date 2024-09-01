export type Quote = {
    assetName: string,
    quote: string,
}

export enum AssetName {
    Undefined = "Undefined",
    EUR_USD = "EUR/USD",
    EUR_JPY = "EUR/JPY",
    USD_JPY = "USD/JPY",
}
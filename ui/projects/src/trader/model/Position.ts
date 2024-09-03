import {AssetName, Quote} from "./Quote";

export type Position = {
    assetName: AssetName;
    side: Side;
    amount: number;
    status: Status;
    quote: Quote;
}

export enum Side {
    Buy = "Buy",
    Sell = "Sell",
    Undefined = "Undefined",
}

export enum Status {
    Open = "Open",
    Pending = "Pending",
    Filled = "Filled",
    Undefined = "Undefined",
}

export const DefaultPositions: Position[] = [
    {
        assetName: AssetName.EUR_JPY,
        side: Side.Buy,
        amount: 300,
        status: Status.Filled,
        quote: {
            assetName: "",
            quote: ""
        }
    },
    {
        assetName: AssetName.EUR_USD,
        side: Side.Buy,
        amount: 400,
        status: Status.Filled,
        quote: {
            assetName: "",
            quote: ""
        }
    },
    {
        assetName: AssetName.EUR_USD,
        side: Side.Buy,
        amount: 250,
        status: Status.Filled,
        quote: {
            assetName: "",
            quote: ""
        }
    },
    {
        assetName: AssetName.EUR_JPY,
        side: Side.Sell,
        amount: 700,
        status: Status.Filled,
        quote: {
            assetName: "",
            quote: ""
        }
    },
]
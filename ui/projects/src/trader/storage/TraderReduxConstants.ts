import {AssetName, Quote} from "../model/Quote";
import {AccountBalance} from "../model/Account";

export type TraderReduxSlice = {
    message: Quote,
    assets: string[],
    accountBalances: AccountBalance[]
}
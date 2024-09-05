import {Quote} from "../model/Quote";
import {AccountBalance} from "../model/Account";
import {Views} from "../model/Views";

export type TraderReduxSlice = {
    message: Quote,
    assets: string[],
    accountBalances: AccountBalance[],
    selectedView: Views
}
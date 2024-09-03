import {createSlice, PayloadAction} from "@reduxjs/toolkit";
import {TraderReduxSlice} from "./TraderReduxConstants";
import {AssetName, Quote} from "../model/Quote";
import {AccountBalance, DefaultAccountBalance} from "../model/Account";
const initialState: TraderReduxSlice = {
    message: {
        assetName: "",
        quote: ""
    },
    assets: [],
    accountBalances: DefaultAccountBalance.accountBalance
};

export const traderReduxSlice = createSlice({
    name: "traderMetaData",
    initialState,
    reducers: {
        updateMessage: (state, action: PayloadAction<Quote>) => {
            state.message = action.payload;
        },
        updateActiveAssets: (state, action:PayloadAction<string[]>) => {
            state.assets = action.payload;
        },
        updateAccountBalance: (state, action:PayloadAction<AccountBalance[]>) => {
            state.accountBalances = action.payload;
        }
    },
});

export const {
    updateMessage,
    updateActiveAssets,
    updateAccountBalance
} = traderReduxSlice.actions;
export default traderReduxSlice.reducer;
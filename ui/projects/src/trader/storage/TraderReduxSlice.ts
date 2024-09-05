import {createSlice, PayloadAction} from "@reduxjs/toolkit";
import {TraderReduxSlice} from "./TraderReduxConstants";
import {Quote} from "../model/Quote";
import {AccountBalance, DefaultAccountBalance} from "../model/Account";
import {Views} from "../model/Views";
const initialState: TraderReduxSlice = {
    message: {
        assetName: "",
        quote: ""
    },
    assets: [],
    accountBalances: DefaultAccountBalance.accountBalance,
    selectedView: Views.TradeView
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
        },
        updateSelectedView: (state, action:PayloadAction<Views>) => {
            state.selectedView = action.payload;
        }
    },
});

export const {
    updateMessage,
    updateActiveAssets,
    updateAccountBalance,
    updateSelectedView
} = traderReduxSlice.actions;
export default traderReduxSlice.reducer;
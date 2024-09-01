import {createSlice, PayloadAction} from "@reduxjs/toolkit";
import {TraderReduxSlice} from "./TraderReduxConstants";
import {Quote} from "../model/Quote";
const initialState: TraderReduxSlice = {
    message: {
        assetName: "",
        quote: ""
    }
};

export const traderReduxSlice = createSlice({
    name: "traderMetaData",
    initialState,
    reducers: {
        updateMessage: (state, action: PayloadAction<Quote>) => {
            state.message = action.payload;
        }
    },
});

export const {
    updateMessage
} = traderReduxSlice.actions;
export default traderReduxSlice.reducer;
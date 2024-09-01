import { configureStore} from "@reduxjs/toolkit";
import traderMetaDataReducer from "./TraderReduxSlice"

export const TraderReduxStore = configureStore({
    reducer: {
        traderMetaData: traderMetaDataReducer
    },
});

export type RootState = ReturnType<typeof TraderReduxStore.getState>;
export type AppDispatch = typeof TraderReduxStore.dispatch;
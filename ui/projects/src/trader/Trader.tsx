import React, {FC} from 'react';
import {TraderReduxStore} from "./storage/TraderReduxStore";
import {Provider} from "react-redux";
import {TraderHomePage} from "./TraderHomePage";

export type TraderProps = {}
export const Trader: FC<TraderProps> = (props) => {
    return (
        <>
            <Provider store={TraderReduxStore}>
                <TraderHomePage />
            </Provider>
        </>
    )
}
import React, {FC} from "react";
import {useAppSelector} from "../../storage/TraderReduxHooks";
import {Views} from "../../model/Views";
import {PositionsView} from "../../views/PositionsView";
import {TradeView} from "../../views/TradeView";
import {AccountView} from "../../views/AccountView";

export type ViewProps = {}

export const View: FC<ViewProps> = () => {
    const appMetaData = useAppSelector( state => {return state;})
    const getSelectedView = () => {
        if (appMetaData.traderMetaData.selectedView === Views.PositionView) {
            return <PositionsView/>
        } else if (appMetaData.traderMetaData.selectedView === Views.AccountView) {
            return <AccountView/>
        } else {
            return <TradeView/>
        }
    }

    return (
        <>
            {getSelectedView()}
        </>
    )
}
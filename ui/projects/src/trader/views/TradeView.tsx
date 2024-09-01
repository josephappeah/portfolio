import React, {FC} from 'react';
import {QuoteCardManager} from "../components/quote/QuoteCardManager";

export type TradeViewProps = {}
export const TradeView:FC<TradeViewProps> = (props) => {
    return (
        <>
            <QuoteCardManager/>
        </>
    )
}
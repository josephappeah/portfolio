import React, {FC} from 'react';
import {Trader} from "../trader/Trader";

export type PortfolioProps = {}
export const Portfolio:FC<PortfolioProps> = (props) => {
    return (
        <>
            <Trader />
        </>
    )
}
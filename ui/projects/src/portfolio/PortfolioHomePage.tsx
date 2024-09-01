import React, {FC} from 'react';
import {Trader} from "../trader/Trader";

export type PortfolioHomePageProps = {}
export const PortfolioHomePage: FC<PortfolioHomePageProps> = (props) => {
    return (
        <>
            <Trader/>
        </>
    )
}
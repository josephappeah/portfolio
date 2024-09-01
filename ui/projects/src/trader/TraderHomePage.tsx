import React, {FC} from 'react';
import {Tabs, TabsContent, TabsList, TabsTrigger} from "../components/ui/tabs"
import {AccountView} from "./views/AccountView";
import {TradeView} from "./views/TradeView";
import {PositionsView} from "./views/PositionsView";

export type TraderHomePageProps = {}
export const TraderHomePage: FC<TraderHomePageProps> = (props) => {
    return (
        <>
            <Tabs defaultValue="trade" className="w-[100%] px-5 py-5">
                <TabsList className="grid w-full grid-cols-3">
                    <TabsTrigger value="account">Account</TabsTrigger>
                    <TabsTrigger value="trade">Trade</TabsTrigger>
                    <TabsTrigger value="pnl">Positions</TabsTrigger>
                </TabsList>
                <TabsContent value="account">
                    <AccountView/>
                </TabsContent>
                <TabsContent value="trade">
                    <TradeView/>
                </TabsContent>
                <TabsContent value="pnl">
                    <PositionsView/>
                </TabsContent>
            </Tabs>
        </>
    )
}
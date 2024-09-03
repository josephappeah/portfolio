import React, {FC, useEffect, useState} from 'react';
import {Card, CardContent, CardFooter, CardHeader, CardTitle} from "../../../components/ui/card";
import {Button} from "../../../components/ui/button";
import {
    Dialog,
    DialogContent,
    DialogFooter,
    DialogHeader,
    DialogTitle,
    DialogTrigger
} from "../../../components/ui/dialog"
import {useAppDispatch, useAppSelector} from "../../storage/TraderReduxHooks";
import {Label} from "../../../components/ui/label";
import {Input} from "../../../components/ui/input";
import TraderDao from "../../dao/TraderDao";
import {AssetName, Quote} from "../../model/Quote";
import {Position, Side, Status} from "../../model/Position";
import {QuoteValidation} from "./QuoteValidation";
import {AccountBalance, DefaultAccountBalance} from "../../model/Account";
import {updateAccountBalance} from "../../storage/TraderReduxSlice";

export type QuoteCardProps = {
    assetName: AssetName;
}
export const QuoteCard: FC<QuoteCardProps> = (props) => {
    const [quote, setQuote] = useState<string>("");
    const [isLoading, setIsLoading] = useState(true);
    const [side, setSide] = useState<Side>(Side.Buy);
    const [to, setTo] = useState<number>(1);
    const reduxPublisher = useAppDispatch()
    const [from, setFrom] = useState<number>(1);
    const [accountBalance, setAccountBalance] = useState<AccountBalance[]>(DefaultAccountBalance.accountBalance)
    let isLoadingTimer: string | number | NodeJS.Timeout | undefined;
    const resetIsLoadingTimer = () => {
        if (isLoading) {
            setIsLoading(false);
        }
        clearTimeout(isLoadingTimer);
        isLoadingTimer = setTimeout(() => setIsLoading(true), 5000);
    }
    const appMetaData = useAppSelector( state => {
        if (state.traderMetaData.message.quote !== "") {
            resetIsLoadingTimer();
        }
        return state;
    })

    useEffect(() => {
        if(appMetaData.traderMetaData.message.assetName === props.assetName) {
            setQuote(appMetaData.traderMetaData.message.quote)
            console.log(appMetaData.traderMetaData.accountBalances)
            setAccountBalance(appMetaData.traderMetaData.accountBalances)
            updateToFrom()
        }
    }, [appMetaData.traderMetaData.message, props.assetName]);

    const updateAccountBalances = () => {
        const myAccountBalance = QuoteValidation.updateAccountBalances(
            props.assetName, accountBalance, to, from
        )
        TraderDao.updateAccountBalance(myAccountBalance)
        reduxPublisher(updateAccountBalance(myAccountBalance))

    }

    const handleNewPosition = () => {
        if(QuoteValidation.canTrade(props.assetName, side, side === Side.Buy? from : to, accountBalance)) {
            const myQuote: Quote = {assetName: props.assetName, quote: quote}
            const myPosition: Position = {
                amount: side === Side.Buy? from : to,
                assetName: props.assetName,
                quote: myQuote,
                side: side,
                status: Status.Filled
            }
            TraderDao.newPosition(myQuote, myPosition)
            updateAccountBalances()
        } else {
            alert("Insufficient Funds")
        }
    }

    const updateToFrom = () => {
        const ratio = quote !== "" ? parseFloat(quote) : 1;
        if (side === Side.Buy) {
            setTo(from * ratio)
        } else {
            setFrom(to / ratio)
        }
    }


    return (
        <>
            <Dialog>
                <Card>
                    <CardHeader>
                        <CardTitle className="grid justify-items-center font-normal">{props.assetName}</CardTitle>
                    </CardHeader>
                    <CardContent className="grid justify-items-center font-extrabold text-4xl">
                        {quote}
                    </CardContent>
                    <CardFooter className="grid w-full grid-cols-2">
                        <DialogTrigger asChild><Button className="mx-2"
                                                       onClick={()=> setSide(Side.Buy)}>Buy</Button></DialogTrigger>
                        <DialogTrigger asChild><Button className="mx-2"
                                                       variant="outline" onClick={()=> setSide(Side.Sell)}>Sell</Button></DialogTrigger>
                    </CardFooter>
                </Card>
                <DialogContent className="sm:max-w-[425px]">
                    <DialogHeader>
                        <DialogTitle>{side} <i>{props.assetName}</i> @ {quote}</DialogTitle>
                    </DialogHeader>
                    <div className="grid gap-2 py-2">
                        <div className="space-y-1">
                            <Label htmlFor="current">{props.assetName.split("/")[0]}</Label>
                            <Input id="current" type="number" value={from} onChange={(e) => {
                                setFrom(parseInt(e.target.value)); updateToFrom();
                                }}/>
                        </div>
                        <div className="space-y-1">
                            <Label htmlFor="current">{props.assetName.split("/")[1]}</Label>
                            <Input id="current" type="number" value={to} onChange={(e) => {
                                setTo(parseInt(e.target.value)); updateToFrom();
                            }}/>
                        </div>
                    </div>
                    <DialogFooter className="grid w-full grid-cols-2">
                        <DialogTrigger asChild><Button variant="outline" type="submit">Cancel</Button></DialogTrigger>
                        <Button type="submit" onClick={()=> handleNewPosition()}>{side}</Button>
                    </DialogFooter>
                </DialogContent>
            </Dialog>
        </>
    )
}
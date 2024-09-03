import React, {FC, ReactElement, useEffect, useState} from 'react';
import {QuoteCard} from "./QuoteCard";
import {SendMessage} from "react-use-websocket";
import {AssetName, Quote} from "../../model/Quote";
import TraderDao from "../../dao/TraderDao";
import {WebSocketMessage} from "react-use-websocket/dist/lib/types";
import {useAppDispatch, useAppSelector} from "../../storage/TraderReduxHooks";
import {updateActiveAssets, updateMessage} from "../../storage/TraderReduxSlice";
import {WebSocketConnection} from "../sockets/WebSocketConnection";
import {
    DropdownMenu, DropdownMenuCheckboxItem,
    DropdownMenuContent,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuTrigger
} from "../../../components/ui/dropdown-menu";
import { Button } from 'src/components/ui/button';
import {TraderConfig} from "../../configs/Configs";
import {DropdownMenuCheckboxItemProps} from "@radix-ui/react-dropdown-menu";

export type QuoteCardManagerProps = {}
export const QuoteCardManager: FC<QuoteCardManagerProps> = (props) => {
    const [sendMessageHandle, setSendMessageHandle] = useState<SendMessage>();
    const [quoteCards, setQuoteCards] = useState<ReactElement[]>([]);
    const [activeAssets, setActiveAssets] = useState<string[]>([]);
    const reduxPublisher = useAppDispatch()
    const appMetaData = useAppSelector( state => {
        return state;
    })

    useEffect(() => {
        if (appMetaData.traderMetaData.assets.length > 0
            && appMetaData.traderMetaData.assets !== activeAssets
        ) {
            const myActiveAssets = [];
            for (let activeAsset of appMetaData.traderMetaData.assets) {
                handleRequestForQuote(activeAsset as unknown as AssetName)
                myActiveAssets.push(activeAsset);
            }
            setActiveAssets(myActiveAssets);
        }
    }, [appMetaData.traderMetaData.assets]);


    const receiveMessage = (message: Quote) => {
        reduxPublisher(updateMessage(message))
    }

    const sendMessageSetter = (sendMessageHandle: SendMessage): void => {
        setSendMessageHandle(sendMessageHandle)
    }

    const sendMessage = (message:Quote):void => {
        if (sendMessageHandle) {
            sendMessageHandle(message as unknown as WebSocketMessage)
        }
    }

    const handleRequestForQuote = async (assetName: AssetName) => {
        if (!activeAssets.includes(assetName)) {
            const myQuoteCard = [...quoteCards];
            myQuoteCard.push(<QuoteCard key={assetName} assetName={assetName} />)
            setQuoteCards(myQuoteCard)
            await TraderDao.requestForQuote(assetName);
        }
    }

    const onAssetSelectionChanged = (assetName: AssetName) => {
        if (activeAssets.includes(assetName)) {
            const myActiveAssets = [];
            for (let activeAsset of activeAssets) {
                if (activeAsset !== assetName){
                    myActiveAssets.push(activeAsset)
                }
            }
            setActiveAssets(myActiveAssets);
            reduxPublisher(updateActiveAssets(myActiveAssets))
            const activeQuoteCards = [];
            for (let quoteCard of quoteCards) {
                if (quoteCard.key !== assetName){
                    activeQuoteCards.push(quoteCard)
                }
            }
            setQuoteCards(activeQuoteCards);
        } else {
            const myActiveAssets = JSON.parse(JSON.stringify(activeAssets));
            myActiveAssets.push(assetName);
            setActiveAssets(myActiveAssets);
            reduxPublisher(updateActiveAssets(myActiveAssets))
        }
    }

    return (
        <>
            {quoteCards.length >= 1 &&
                <div className="grid w-full grid-cols-4">
                    {quoteCards.length >= 1 && <div className="col-auto px-10 py-10">{quoteCards[0]}</div>}
                    {quoteCards.length >= 2 && <div className="col-auto px-10 py-10">{quoteCards[1]}</div>}
                    {quoteCards.length >= 3 && <div className="col-auto px-10 py-10">{quoteCards[2]}</div>}
                    {quoteCards.length >= 4 && <div className="col-auto px-10 py-10">{quoteCards[3]}</div>}
                </div>
            }
            {quoteCards.length >= 5 &&
                <div className="grid w-full grid-cols-4">
                    {quoteCards.length >= 5 && <div className="col-auto px-10 py-10">{quoteCards[4]}</div>}
                    {quoteCards.length >= 6 && <div className="col-auto px-10 py-10">{quoteCards[5]}</div>}
                    {quoteCards.length >= 7 && <div className="col-auto px-10 py-10">{quoteCards[6]}</div>}
                    {quoteCards.length >= 8 && <div className="col-auto px-10 py-10">{quoteCards[7]}</div>}
                </div>
            }
            <DropdownMenu>
                <DropdownMenuTrigger asChild>
                    <Button variant="outline">Request For Quote</Button>
                </DropdownMenuTrigger>
                <DropdownMenuContent className="w-full">
                    <DropdownMenuLabel>FX</DropdownMenuLabel>
                    <DropdownMenuSeparator />
                    {TraderConfig.TraderService.assets.map(assetName =>
                            <DropdownMenuCheckboxItem
                                key={assetName}
                                checked={activeAssets.includes(assetName)}
                                onCheckedChange={() => onAssetSelectionChanged(assetName)}
                                onClick={() => handleRequestForQuote(assetName)}
                            >
                                {assetName}
                            </DropdownMenuCheckboxItem>
                        )
                    }
                </DropdownMenuContent>
            </DropdownMenu>
            <WebSocketConnection onMessage={receiveMessage} sendMessageCallBack={sendMessageSetter}/>
        </>
    )
}
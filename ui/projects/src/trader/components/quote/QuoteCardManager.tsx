import React, {FC, ReactElement, useState} from 'react';
import {QuoteCard} from "./QuoteCard";
import {SendMessage} from "react-use-websocket";
import {AssetName, Quote} from "../../model/Quote";
import TraderDao from "../../dao/TraderDao";
import {WebSocketMessage} from "react-use-websocket/dist/lib/types";
import {useAppDispatch} from "../../storage/TraderReduxHooks";
import {updateMessage} from "../../storage/TraderReduxSlice";
import {WebSocketConnection} from "../sockets/WebSocketConnection";
import {
    DropdownMenu, DropdownMenuCheckboxItem,
    DropdownMenuContent,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuTrigger
} from "../../../components/ui/dropdown-menu";
import { Button } from 'src/components/ui/button';
import {TraderConfig} from "../../configs/configs";

export type QuoteCardManagerProps = {}
export const QuoteCardManager: FC<QuoteCardManagerProps> = (props) => {
    const [sendMessageHandle, setSendMessageHandle] = useState<SendMessage>();
    const [quoteCards, setQuoteCards] = useState<ReactElement[]>([]);
    const [activeAssets, setActiveAssets] = useState<string[]>([]);
    const reduxPublisher = useAppDispatch()

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
        console.log("an",assetName)
        if (!activeAssets.includes(assetName)) {
            const myQuoteCard = [...quoteCards];
            myQuoteCard.push(<QuoteCard assetName={assetName} />)
            setQuoteCards(myQuoteCard)
            await TraderDao.requestForQuote(assetName);
        }
    }

    const onAssetSelectionChanged = (assetName: string) => {
        if (activeAssets.includes(assetName)) {
            const myActiveAssets = [];
            for (let activeAsset in activeAssets) {
                if (activeAsset !== assetName){
                    myActiveAssets.push(activeAsset)
                }
            }
            setActiveAssets(myActiveAssets);
        } else {
            const myActiveAssets = activeAssets;
            myActiveAssets.push(assetName);
            setActiveAssets(myActiveAssets);
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
                                onClick={() => handleRequestForQuote(assetName)}>
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
import React, {FC, useState} from 'react';
import useWebSocket, {SendMessage} from "react-use-websocket";
import {Quote} from "../../model/Quote";
import {TraderConfig} from "../../configs/Configs";

export type WebSocketConnectionProps =  {
    onMessage: (message: Quote) => void;
    sendMessageCallBack:(sendMessage: SendMessage) => void;
}

export const WebSocketConnection: FC<WebSocketConnectionProps> = (props) => {
    const [isConnected, setIsConnected] = useState<boolean>(false);
    const [isLoading, setIsLoading] = useState<boolean>(false);

    const getWebSocketHost = () => {
        return TraderConfig.TraderService.webSocketService.Host + TraderConfig.TraderService.webSocketService.Port
    }

    const {
        sendMessage,
        sendJsonMessage,
        lastMessage,
        lastJsonMessage,
        readyState,
        getWebSocket,
    } = useWebSocket(getWebSocketHost(), {
        onOpen: () => {
            setIsConnected(true);
            setIsLoading(false);
        },
        onMessage: (msg) => {
            props.onMessage(parseMessage(msg.data))
        },
        shouldReconnect: (closeEvent) => true,
    });

    props.sendMessageCallBack(sendMessage)
    const parseMessage = (message: string): Quote => {
        message = message.replace(/'/g, '"')
        const parsedMessage: any = JSON.parse(message);
        return {
            assetName: parsedMessage.assetName,
            quote: parsedMessage.quote
        }
    }
    return (<></>)
}
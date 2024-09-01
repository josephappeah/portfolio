import {AssetName} from "../model/Quote";

export const TraderConfig = {
    TraderService: {
        webSocketService: {
            Host: "ws://localhost:",
            Port: "8765",
        },
        quoteService: {
            Host: "http://0.0.0.0:",
            Port: "8080"
        },
        dataService:{
            Host: "http://0.0.0.0:",
            Port: "8081"
        },
        paths : {
            RFQ: "/request-for-quote",
            UpdateAccountBalance: "/update-account-balance",
            GetAccountBalance: "/get-account-balance",
            GetPositions: "/get-positions",
            NewPosition: "/new-position",
        },
        assets: [AssetName.EUR_USD, AssetName.EUR_JPY, AssetName.USD_JPY]
    }
}
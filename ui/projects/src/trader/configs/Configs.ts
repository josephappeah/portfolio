import {AssetName} from "../model/Quote";

export const TraderConfig = {
    TraderService: {
        webSocketService: {
            Host: "ws://ec2-54-90-208-49.compute-1.amazonaws.com:",
            Port: "8765",
        },
        quoteService: {
            Host: "http://ec2-54-90-208-49.compute-1.amazonaws.com:",
            Port: "8080"
        },
        dataService:{
            Host: "http://ec2-54-90-208-49.compute-1.amazonaws.com:",
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
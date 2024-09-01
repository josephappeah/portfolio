import axios from "axios";
import {AccountBalance} from "../model/Account";
import {TraderDaoUtils} from "./TraderDaoUtils";
import {Position} from "../model/Position";
import {Quote} from "../model/Quote";

export default class TraderDao {

    public static async requestForQuote(assetName: string): Promise<boolean> {
        return axios.get(
            TraderDaoUtils.getRFQRequestPath(), {
                params: TraderDaoUtils.getRFQRequestParams(assetName)
            }
        ).then(data => {
            //console.log(data);
            return true;
        }).catch(err => {
            console.log(err);
            return false;
        })
    }

    public static async updateAccountBalance(account: AccountBalance[]): Promise<boolean> {
        return axios.get(
            TraderDaoUtils.getUpdateAccountBalanceRequestPath(), {
                params: TraderDaoUtils.getUpdateAccountBalanceRequestParams(account)
            }
        ).then(data => {
            //console.log(data);
            return true;
        }).catch(err => {
            console.log(err);
            return false;
        })
    }

    public static async fetchAccountBalance(accountBalance: AccountBalance[]): Promise<AccountBalance[]> {
        return axios.get(
            TraderDaoUtils.getAccountBalanceRequestPath(), {
                params: TraderDaoUtils.getFetchAccountBalanceRequestParams(accountBalance)
        }).then(data => {
            //console.log(data);
            return TraderDaoUtils.parseAccountBalance(data)
        }).catch(err => {
            console.log(err);
            return []
        });
    }

    public static async fetchPositions(): Promise<Position[]> {
        return axios.get(TraderDaoUtils.getPositionsRequestPath(), {
            params: TraderDaoUtils.getFetchPositionsRequestParams()
        }).then(data => {
            return TraderDaoUtils.parsePositions(data)
        }).catch(err => {
            console.log(err)
            return []
        });
    }

    public static async newPosition(quote: Quote, position: Position): Promise<boolean> {
        return axios.get(
            TraderDaoUtils.getNewPositionRequestPath(), {
                params: TraderDaoUtils.getNewPositionRequestParams(quote, position)
            }
        ).then(data => {
            console.log(data);
            return true;
        }).catch(err => {
            console.log(err);
            return false;
        })
    }
}
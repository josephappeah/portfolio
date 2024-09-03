import {AssetName} from "../../model/Quote";
import {Side} from "../../model/Position";
import {AccountBalance} from "../../model/Account";

export class QuoteValidation {
    public static canTrade(assetName: AssetName, side: Side,
                           amount: number, accountBalances: AccountBalance[]): boolean {
        let currency = ""
        if (side == Side.Buy) {
            currency = assetName.split("/")[0]
        } else {
            currency = assetName.split("/")[1]
        }
        if (accountBalances.length > 0) {
            const accountBalance: AccountBalance[] = accountBalances
                .filter(accountBalance => accountBalance.currency === currency)
            return accountBalance[0].balance > amount;
        } else {
            return false;
        }
    }

    public static updateAccountBalances(
        assetName: AssetName, accountBalances: AccountBalance[],
        toAmount: number, fromAmount: number): AccountBalance[] {
        const toCurrency = assetName.split("/")[1]
        const fromCurrency = assetName.split("/")[0]
        const updatedAccountBalances: AccountBalance[] = []
        for (let accountBalance of accountBalances) {
            accountBalance = accountBalance as unknown as AccountBalance;
            let myAccountBalance: AccountBalance = {
                currency: accountBalance.currency,
                balance: accountBalance.balance,
            };
            if (accountBalance.currency === toCurrency) {
                myAccountBalance = {
                    currency: toCurrency,
                    balance: accountBalance.balance + toAmount,
                }
            } else if (accountBalance.currency === fromCurrency) {
                myAccountBalance = {
                    currency: fromCurrency,
                    balance: accountBalance.balance - fromAmount,
                }
            }
            updatedAccountBalances.push(myAccountBalance);
        }

        return updatedAccountBalances;
    }
}
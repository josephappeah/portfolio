import React, {FC, useEffect, useState} from 'react';
import {Card, CardContent, CardFooter, CardHeader, CardTitle} from "../../components/ui/card";
import {Label} from "../../components/ui/label";
import {Input} from "../../components/ui/input";
import {Button} from "../../components/ui/button";
import {AccountBalance, DefaultAccountBalance} from "../model/Account";
import {TraderUtils} from "../utils/TraderUtils";
import TraderDao from "../dao/TraderDao";
import {useAppDispatch} from "../storage/TraderReduxHooks";
import {updateAccountBalance} from "../storage/TraderReduxSlice";

export type AccountViewProps = {}
export const AccountView:FC<AccountViewProps> = (props) => {
    const [accountBalance, setAccountBalance] = useState<AccountBalance[]>(DefaultAccountBalance.accountBalance);
    const reduxPublisher = useAppDispatch()
    const onAccountReset = async() => {
        await TraderDao.updateAccountBalance(accountBalance);
    }

    const onAccountBalanceChange = (newBalance: AccountBalance) => {
        const accountBalance = [newBalance];
        for (let balance of accountBalance) {
            if (balance.currency !== newBalance.currency) {
                accountBalance.push(balance);
            }
        }
        setAccountBalance(accountBalance)
        reduxPublisher(updateAccountBalance(accountBalance))
    }

    useEffect(() => {
        TraderDao.fetchAccountBalance(accountBalance)
            .then((accountBalance) => {
                //console.log(accountBalance);
                if (accountBalance.length > 0) {
                    setAccountBalance(accountBalance)
                    reduxPublisher(updateAccountBalance(accountBalance))
                } else {
                    setAccountBalance(DefaultAccountBalance.accountBalance)
                    TraderDao.updateAccountBalance(DefaultAccountBalance.accountBalance);
                    reduxPublisher(updateAccountBalance(accountBalance))
                }
            }).catch((err) => {
                console.log(err);
            })
    }, []);

    return (
        <div className="px-10">
            <Card>
                <CardHeader>
                    <CardTitle className="text-2xl">Accounts</CardTitle>
                </CardHeader>
                <CardContent className="space-y-2">
                    {
                        accountBalance.map(balance =>
                            <div key={balance.currency} className="grid w-full items-center gap-1.5 py-2">
                                <Label htmlFor="currency" className="font-medium">
                                    {balance.currency} ({TraderUtils.currencyToCurrencySymbol(balance.currency)})
                                </Label>
                                <Input type="number" placeholder={balance.balance.toString()}
                                    onChange={(e) => {
                                        onAccountBalanceChange({
                                            balance: parseInt(e.target.value),
                                            currency: balance.currency,
                                        })
                                    }
                                }
                                />
                            </div>
                        )
                    }
                </CardContent>
                <CardFooter>
                    <Button variant="outline" onClick={() => onAccountReset()}>Update Account Balance</Button>
                </CardFooter>
            </Card>
        </div>
    )
}
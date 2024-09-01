import React, {FC, useEffect, useState} from 'react';
import {Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle} from "../../components/ui/card";
import {Label} from "../../components/ui/label";
import {Input} from "../../components/ui/input";
import {Button} from "../../components/ui/button";
import {AccountBalance, DefaultAccountBalance} from "../model/Account";
import {TraderUtils} from "../utils/TraderUtils";
import TraderDao from "../dao/TraderDao";

export type AccountViewProps = {}
export const AccountView:FC<AccountViewProps> = (props) => {
    const [accountBalance, setAccountBalance] = useState<AccountBalance[]>(DefaultAccountBalance.accountBalance);

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
    }

    useEffect(() => {
        TraderDao.fetchAccountBalance(accountBalance)
            .then((accountBalance) => {
                //console.log(accountBalance);
                if (accountBalance.length > 0) {
                    setAccountBalance(accountBalance)
                } else {
                    setAccountBalance(DefaultAccountBalance.accountBalance)
                    TraderDao.updateAccountBalance(DefaultAccountBalance.accountBalance);
                }
            }).catch((err) => {
                console.log(err);
            })
    }, []);

    return (
        <>
            <Card>
                <CardHeader>
                    <CardTitle>Accounts</CardTitle>
                    <CardDescription>
                        How much of each currency you have to trade
                    </CardDescription>
                </CardHeader>
                <CardContent className="space-y-2">
                    {
                        accountBalance.map(balance =>
                            <div key={balance.currency} className="grid w-full items-center gap-1.5">
                                <Label htmlFor="email">
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
                    <Button onClick={() => onAccountReset()}>Reset</Button>
                </CardFooter>
            </Card>
        </>
    )
}
import React, {FC, useEffect, useState} from 'react';
import {
    Table,
    TableBody,
    TableCaption,
    TableCell,
    TableFooter,
    TableHead,
    TableHeader,
    TableRow
} from "../../components/ui/table";
import {Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle} from "../../components/ui/card";
import {Position} from "../model/Position";
import TraderDao from "../dao/TraderDao";

export type PositionsView = {}

export const PositionsView:FC<PositionsView> = (props) => {
    const [positions, setPositions] = useState<Position[]>([])

    useEffect(() => {
        TraderDao.fetchPositions()
            .then((positions) => setPositions(positions))
            .catch((err) => console.error(err));
    }, []);

    return (
        <>
            <Card>
                <CardHeader>
                    <CardTitle>Positions</CardTitle>
                    <CardDescription>
                    </CardDescription>
                </CardHeader>
                <CardContent className="space-y-2">
                    <Table>
                        <TableCaption></TableCaption>
                        <TableHeader>
                            <TableRow>
                                <TableHead className="w-[100px]">Asset</TableHead>
                                <TableHead>Side</TableHead>
                                <TableHead>Amount</TableHead>
                                <TableHead className="text-right">Status</TableHead>
                            </TableRow>
                        </TableHeader>
                        <TableBody>
                            {positions.map((position) => (
                                <TableRow key={position.assetName}>
                                    <TableCell className="font-medium">{position.assetName}</TableCell>
                                    <TableCell>{position.side}</TableCell>
                                    <TableCell>{position.amount}</TableCell>
                                    <TableCell className="text-right">{position.status}</TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                        <TableFooter className="grid w-full">
                            <TableRow className="grid w-full" >
                                {/*{positions.length == 0 && "No Positions. Add Positions on the Trade Tab"}*/}
                            </TableRow>
                        </TableFooter>
                    </Table>
                </CardContent>
                <CardFooter>
                </CardFooter>
            </Card>
        </>
    )
}
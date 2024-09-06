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

export type PositionsViewProps = {}

export const PositionsView:FC<PositionsViewProps> = (props) => {
    const [positions, setPositions] = useState<Position[]>([])

    useEffect(() => {
        TraderDao.fetchPositions()
            .then((positions) => setPositions(positions))
            .catch((err) => console.error(err));
    }, []);

    return (
        <div className="px-10">
            <Card>
                <CardHeader>
                    <CardTitle className="text-2xl">Positions</CardTitle>
                    <CardDescription>
                    </CardDescription>
                </CardHeader>
                <CardContent className="space-y-2">
                    <Table>
                        <TableCaption></TableCaption>
                        <TableHeader>
                            <TableRow>
                                <TableHead className="text-center">Asset</TableHead>
                                <TableHead className="text-center">Side</TableHead>
                                <TableHead className="text-center">Amount</TableHead>
                                <TableHead className="text-center">Status</TableHead>
                            </TableRow>
                        </TableHeader>
                        <TableBody>
                            {positions.map((position) => (
                                <TableRow key={position.assetName}>
                                    <TableCell className="text-center">{position.assetName}</TableCell>
                                    <TableCell className="text-center">{position.side}</TableCell>
                                    <TableCell className="text-center">{position.amount}</TableCell>
                                    <TableCell className="text-center">{position.status}</TableCell>
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
        </div>
    )
}
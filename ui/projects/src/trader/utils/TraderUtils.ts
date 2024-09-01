import {Currency, CurrencyToCurrencySymbolMap} from "../model/Account";

export class TraderUtils {

    public static currencyToCurrencySymbol(currency: Currency): string {
        if (Object.keys(CurrencyToCurrencySymbolMap).includes(currency)){
            return CurrencyToCurrencySymbolMap[currency];
        }
        return "$"
    }
}
import sqlite3
import yfinance as yf
import datetime

import itertools
import functools
import toolz

import pandas as pd
import numpy as np

ISHARES_ETF = {
    'CSPX.L': {'name': 'iShares Core S&P 500 UCITS ETF'},
    'CNDX.L': {'name': 'iShares NASDAQ 100 UCITS ETF'},
    'IWDG.L': {'name': 'iShares Core MSCI World UCITS ETF'},
    'SWDA.L': {'name': 'iShares Core MSCI World UCITS ETF'},
    'CNKY.L': {'name': 'iShares Nikkei 225 UCITS ETF'},
    'EIMI.L': {'name': 'iShares Core MSCI EM IMI UCITS ETF'},
    'IMEU.L': {'name': 'iShares Core MSCI Europe UCITS ETF'},
    'CSX5.L': {'name': 'iShares Core EURO STOXX 50 UCITS ETF'},
    'SSAC.L': {'name': 'iShares MSCI ACWI UCITS ETF'},
    'SGWS.L': {'name': 'iShares MSCI World SRI UCITS ETF'},
    'ISF.L':  {'name': 'iShares Core FTSE 100 UCITS ETF'},
    'MIDD.L': {'name': 'iShares FTSE 250 UCITS ETF'},
    'IUKP.L': {'name': 'iShares UK Property UCITS ETF'},
    'IBTU.L': {'name': 'iShares $ Treasury Bond 0-1yr UCITS ETF'},
    'IBTS.L': {'name': 'iShares $ Treasury Bond 1-3yr UCITS ETF'},
    'CBUG.L': {'name': 'iShares $ Treasury Bond 3-7yr UCITS ETF'},
    'IBTM.L': {'name': 'iShares $ Treasury Bond 7-10yr UCITS ETF'},
    'IDTG.L': {'name': 'iShares $ Treasury Bond 20+yr UCITS ETF'},
    'ITPG.L': {'name': 'iShares $ TIPS UCITS ETF'},
    'IGLS.L': {'name': 'iShares UK Gilts 0-5yr UCITS ETF'},
    'IGLT.L': {'name': 'iShares Core UK Gilts UCITS ETF'},
    'INXG.L': {'name': 'iShares £ Index-Linked Gilts UCITS ETF'},
    'LQDE.L': {'name': 'iShares $ Corp Bond UCITS ETF'},
    'AGBP.L': {'name': 'iShares Core Global Aggregate Bond UCITS ETF'},
    'IHYG.L': {'name': 'iShares € High Yield Corp Bond UCITS ETF'},
    'IEMB.L': {'name': 'iShares J.P. Morgan $ EM Bond UCITS ETF'},
    'SEGA.L': {'name': 'iShares Core € Govt Bond UCITS ETF'},
    'IEAC.L': {'name': 'iShares Core € Corp Bond UCITS ETF'},
    'SGLN.L': {'name': 'iShares Physical Gold ETC'},
    'SSLN.L': {'name': 'iShares Physical Silver ETC'},
    'SPLT.L': {'name': 'iShares Physical Platinum ETC'},
    'SPDM.L': {'name': 'iShares Physical Palladium ETC'},
}

def main():
    
    current_datetime = datetime.datetime.now()

    etf_tickers = yf.Tickers(list(ISHARES_ETF.keys()))
    etf_prices = etf_tickers.history(period='1d', interval='5m', actions=False)

    etf_prices_melted = etf_prices.melt(var_name=['metric', 'ticker'], ignore_index=False)

    etf_prices_melted['time_added'] = current_datetime

    con = sqlite3.connect('equity.db')

    etf_prices_melted.to_sql(
        name = 'blackrock_etf',
        con=con,
        if_exists='append'
    )

    print(etf_prices_melted)

    return 0


if __name__ == '__main__':
    main()

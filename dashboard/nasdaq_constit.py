import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc

import pandas as pd
import numpy as np

import requests
import functools as ft
import itertools as it

from bs4 import BeautifulSoup
# from lxml import html

import yfinance as yf

NASDAQ_CONSTIT_URL = 'https://en.wikipedia.org/wiki/Nasdaq-100'

def render():
    return html.Div([
        dbc.Select(
            id="index-select",
            options=[
                {"label": "Nasdaq100", "value": "nasdaq100"},
            ],
        ),
        dash_table.DataTable(
            id='nasdaq100-constit-table',
            style_table={
                'width': '80%'
            },
            style_header={
                'backgroundColor': 'rgb(18, 18, 18)',
                'color': 'white'
            },
            style_data={
                'backgroundColor': 'rgb(0, 0, 0)',
                'color': 'white'
            },
        )
    ])

@callback(
    Output('nasdaq100-constit-table', 'data'),
    [
        Input('index-select', 'value')
    ]
    
)
def render_table(selected):
    logger.debug('hello', selected)
    df_constit = get_nasdaq_constit()
    
    return df_constit.to_dict('records')


@ft.cache
def get_nasdaq_constit():
    '''
    '''

    response = requests.get(NASDAQ_CONSTIT_URL, headers={"User-Agent":"Mozilla/5.0"})
    logger.info(f'Wikipedia responded with status code: {response.status_code} for S&P600 table.')
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'class': 'wikitable', 'id': 'constituents'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    header = rows[0]
    body = rows[1:]

    col_names = [x.get_text().replace('\n', '') for x in header.find_all('th')]

    data = []
    for row in body:
        columns = [col.get_text().replace('\n', '') for col in row.find_all('td')]
        data.append(columns)

    df = pd.DataFrame(data, columns=col_names)
    logger.info(df)

    df = df[['Company', 'Ticker', 'GICS Sector', 'GICS Sub-Industry']]
    df.columns = ['company', 'ticker', 'industry', 'subindustry']

    return df

def main():
    df_constit = get_nasdaq_constit()
    return 0

if __name__ == '__main__':
    main()
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

import flask
from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc

import plotly.express as px
import pandas as pd

server = flask.Flask(__name__)

app = Dash(
    __name__, 
    server=server,
    external_stylesheets=[dbc.themes.CYBORG],
    suppress_callback_exceptions=True
)

## IP = 158.220.82.151

import nasdaq_constit

app.layout = html.Div(
    children=[
        dbc.Tabs(
            [
                dbc.Tab(label="Home", tab_id="home"),
                dbc.Tab(label="Nasdaq100 Constituents", tab_id="nasdaq100-constit"),
            ],
            id="tabs-selection",
            active_tab="home",
        ),
        html.H4('Hello there !'),
        html.Div(id="tabs-selection-content"),
    ],
    className='dbc'
)

@callback(
    Output('tabs-selection-content', 'children'),
    [
        Input('tabs-selection', 'active_tab')
    ]
)
def render(tab):
    logger.debug(tab)

    if tab == 'home':
        return html.H4('Welcome')
    elif tab == 'nasdaq100-constit':
        return nasdaq_constit.render()
    else:
        raise ValueError()

if __name__ == '__main__':
    app.run(debug=True)
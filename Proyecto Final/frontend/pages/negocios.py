import dash
import dash_svg
import pandas as pd
import plotly.express as px
from dash import html, dcc, callback, Input, Output, State, ALL

backend_url = "http://127.0.0.1:8000"

dash.register_page(__name__,
                   path="/negocios",
                   title="Vista de negocios",
                   name="negocios")

layout = html.Div(
    className="bg-gray-50",
    children=[
        html.Main(
            className="mx-auto min-h-screen max-w-7xl px-4 py-10 text-gray-700",
            children=[
                html.Section(
                    className="flex flex-col rounded-lg bg-white p-6 shadow-lg",
                    children=[
                        html.Div(
                            className="mb-4 flex justify-center",
                            children=[
                                dcc.Input(id="search-terms",
                                          className="w-96 rounded-l-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring focus:ring-blue-300"),
                                html.Button(
                                    id="search-button",
                                    className="rounded-r-lg bg-blue-600 px-4 text-white hover:bg-blue-700 focus:outline-none focus:ring focus:ring-blue-300",
                                    children=["Buscar"],
                                )
                            ],
                        ),
                        dcc.Loading(children=[
                            html.Div(id="search-results")
                        ]),
                        dcc.Loading(children=[
                            html.Div(id="restaurant-details")
                        ]),
                    ]
                )
            ]
        )
    ]
)
import dash
import dash_svg
import pandas as pd
import plotly.express as px
import requests
from dash import html, dcc, callback, Input, Output, State, ALL, ctx

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
                                dcc.Input(
                                    id="search-terms",
                                    className="w-96 rounded-l-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring focus:ring-blue-300"),
                                html.Button(
                                    id="search-button",
                                    className="rounded-r-lg bg-blue-600 px-4 text-white hover:bg-blue-700 focus:outline-none focus:ring focus:ring-blue-300",
                                    children=["Buscar"],
                                )
                            ],
                        ),
                        dcc.Loading(
                            id="loading-search-results",
                            children=[
                                html.Div(id="search-results")
                                ]),
                        dcc.Loading(
                            id="loading-restaurant-details",
                            children=[
                                html.Div(id="restaurant-details")
                                ]),
                    ]
                )
            ]
        )
    ]
)

@callback(
    Output("search-results", "children"),
    Input("search-button", "n_clicks"),
    State("search-terms", "value")
)
def search_restaurants(n_clicks, search_terms):
    if n_clicks is None:
        return ""
    else:
        if not search_terms:
            return html.Div(
                className="text-center",
                children=[
                    html.P(
                        className="font-semibold text-red-700 text-lg",
                        children=["Debes introducir los términos que deseas buscar."])
                ]
                )
        try:
            search_url = f"{backend_url}/restaurant_search"
            data = {
                "terms": search_terms
            }
            search_response = requests.post(search_url, json=data)
            search_results = search_response.json()
            return html.Ul(
                        className="mb-4 space-y-4",
                        children=[
                            html.Li(
                                className="flex flex-col items-center justify-between rounded-lg bg-white p-4 shadow-md md:flex-row",
                                children=[
                                    html.Span(
                                        className="text-lg font-semibold text-gray-700",
                                        children=[restaurant["Name"]],
                                    ),
                                    html.Button(
                                        id={"type":"restaurant-button", "index":restaurant["rowid"]},
                                        className="rounded-lg bg-gradient-to-br from-teal-400 to-blue-500 px-6 py-3 font-semibold text-white hover:from-pink-300 hover:to-orange-600",
                                        children=["Ver restaurante"],
                                    ),
                                ],
                            ) for restaurant in search_results],
                    )
        except Exception as e:
            return html.Div(
                className="text-center",
                children=[
                    html.P(className="font-semibold text-red-700 text-lg",
                           children=["Hubo un error en la comunicación con el servidor."])
                ]
                )
            
@callback(
    Output("restaurant-details", "children"),
    Input({"type": "restaurant-button", "index": ALL}, "n_clicks"),
    State({"type": "restaurant-button", "index": ALL}, "id"),
)
def show_restaurant_details(n_clicks, restaurant_id):
    if not any(n_clicks):
        return ""
    try:
        id = ctx.triggered_id["index"]
        restaurant_url = f"{backend_url}/restaurant/{id}"
        restaurant_response = requests.get(restaurant_url)
        restaurant = restaurant_response.json()
        
        transactions_url = f"{backend_url}/transactions"
        end_date = pd.Timestamp.today()
        start_date = pd.Timestamp.today() - pd.DateOffset(months=2)
        data = {
            "restaurant_id": id,
            "start_date": start_date.date().isoformat(),
            "end_date": end_date.date().isoformat()
        }
        transactions_response = requests.post(transactions_url, json=data)
        transactions = transactions_response.json()
        transactions_df = pd.DataFrame(transactions)
        transactions_df["Timestamp"] = pd.to_datetime(transactions_df["Timestamp"])
        
        start_month_tips = transactions_df[transactions_df["Timestamp"].dt.month == start_date.month]["Tip"].sum()
        end_month_tips = transactions_df[transactions_df["Timestamp"].dt.month == end_date.month]["Tip"].sum()
        
        delta_tip = (end_month_tips - start_month_tips) / start_month_tips * 100
            
        delta_color = "text-green-700" if delta_tip > 0 else "text-red-700" if delta_tip < 0 else "text-gray-700"
        
        payment_icon = {
            "Credit Card": "M2.25 8.25h19.5M2.25 9h19.5m-16.5 5.25h6m-6 2.25h3m-3.75 3h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Z",
            "Debit Card": "M2.25 8.25h19.5M2.25 9h19.5m-16.5 5.25h6m-6 2.25h3m-3.75 3h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Z",
            "Cash": "M2.25 18.75a60.07 60.07 0 0 1 15.797 2.101c.727.198 1.453-.342 1.453-1.096V18.75M3.75 4.5v.75A.75.75 0 0 1 3 6h-.75m0 0v-.375c0-.621.504-1.125 1.125-1.125H20.25M2.25 6v9m18-10.5v.75c0 .414.336.75.75.75h.75m-1.5-1.5h.375c.621 0 1.125.504 1.125 1.125v9.75c0 .621-.504 1.125-1.125 1.125h-.375m1.5-1.5H21a.75.75 0 0 0-.75.75v.75m0 0H3.75m0 0h-.375a1.125 1.125 0 0 1-1.125-1.125V15m1.5 1.5v-.75A.75.75 0 0 0 3 15h-.75M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Zm3 0h.008v.008H18V10.5Zm-12 0h.008v.008H6V10.5Z",
            "Mobile Payment": "M10.5 1.5H8.25A2.25 2.25 0 0 0 6 3.75v16.5a2.25 2.25 0 0 0 2.25 2.25h7.5A2.25 2.25 0 0 0 18 20.25V3.75a2.25 2.25 0 0 0-2.25-2.25H13.5m-3 0V3h3V1.5m-3 0h3m-3 18.75h3",
            "default": "M12 6v12m-3-2.818.879.659c1.171.879 3.07.879 4.242 0 1.172-.879 1.172-2.303 0-3.182C13.536 12.219 12.768 12 12 12c-.725 0-1.45-.22-2.003-.659-1.106-.879-1.106-2.303 0-3.182s2.9-.879 4.006 0l.415.33M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"
        }
        
        daily_transactions = transactions_df.groupby(transactions_df["Timestamp"].dt.date)["Tip"].sum().reset_index()
        
        fig = px.line(daily_transactions, x="Timestamp", y="Tip", labels={"Timestamp": "Fecha", "Tip": "Propinas"})
        
        return html.Div(children=[
            html.Div(
                className="text-center",
                children=[
                    html.H2(
                        className="mb-4 text-6xl font-bold mt-6",
                        children=restaurant["Name"],
                    ),
                    html.P(
                        className="mb-4 text-justify font-semibold text-xl",
                        children=restaurant["Details"],
                    ),
                ],
            ),
            html.Img(
                className="mb-4 rounded-lg shadow-lg",
                src=f"{backend_url}/restaurant/{id}/image",
                alt=f"Imagen del restaurante {restaurant['Name']}",
            ),
            html.Div(
                className="mb-4 rounded-lg p-6 text-center shadow-lg",
                children=[
                    html.H3(
                        className="mb-4 text-4xl font-semibold",
                        children=["Indicadores de los últimos 3 meses"],
                    ),
                    html.Div(
                        className="grid grid-cols-1 gap-6 md:grid-cols-4",
                        children=[
                            html.Div(
                                className="rounded-lg p-6 shadow-lg",
                                children=[
                                    html.H4(
                                        className="mb-2 text-xl font-semibold",
                                        children=["Personal registrado"],
                                    ),
                                    html.P(
                                        className="mb-2 text-6xl font-bold",
                                        children=[
                                            transactions_df["Waiter"].nunique(),
                                            dash_svg.Svg(
                                                xmlns="http://www.w3.org/2000/svg",
                                                fill="none",
                                                viewBox="0 0 24 24",
                                                stroke="currentColor",
                                                className="inline h-14 w-14",
                                                children=[
                                                    dash_svg.Path(
                                                        strokeLinecap="round",
                                                        strokeLinejoin="round",
                                                        d="M15 19.128a9.38 9.38 0 0 0 2.625.372 9.337 9.337 0 0 0 4.121-.952 4.125 4.125 0 0 0-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 0 1 8.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0 1 11.964-3.07M12 6.375a3.375 3.375 0 1 1-6.75 0 3.375 3.375 0 0 1 6.75 0Zm8.25 2.25a2.625 2.625 0 1 1-5.25 0 2.625 2.625 0 0 1 5.25 0Z",
                                                    )
                                                ],
                                            ),
                                        ],
                                    ),
                                    html.P(
                                        children=[
                                            "Cuentas activas"
                                        ]
                                    ),
                                ],
                            ),
                            html.Div(
                                className="rounded-lg p-6 shadow-lg",
                                children=[
                                    html.H4(
                                        className="mb-2 text-xl font-semibold",
                                        children=["Propinas obtenidas"],
                                    ),
                                    html.P(
                                        className=f"mb-2 text-6xl font-bold {delta_color}",
                                        children=[f"{delta_tip:.0f}%"],
                                    ),
                                    html.P(
                                        children=["3 meses a la fecha"]
                                    ),
                                ],
                            ),
                            html.Div(
                                className="rounded-lg p-6 shadow-lg",
                                children=[
                                    html.H4(
                                        className="mb-2 text-xl font-semibold",
                                        children=["Promedio"],
                                    ),
                                    html.P(
                                        className="mb-2 text-6xl font-bold",
                                        children=[f"${transactions_df['Tip'].mean():,.2f}"],
                                    ),
                                    html.P(children=["Por propina"]),
                                ],
                            ),
                            html.Div(
                                className="rounded-lg p-6 shadow-lg",
                                children=[
                                    html.H4(
                                        className="mb-2 text-xl font-semibold",
                                        children=["Método de pago más usado"],
                                    ),
                                    html.P(
                                        className="mb-2 text-6xl font-bold",
                                        children=[
                                            dash_svg.Svg(
                                                xmlns="http://www.w3.org/2000/svg",
                                                fill="none",
                                                viewBox="0 0 24 24",
                                                stroke="currentColor",
                                                className="inline h-14 w-14",
                                                children=[
                                                    dash_svg.Path(
                                                        strokeLinecap="round",
                                                        strokeLinejoin="round",
                                                        d=payment_icon.get(transactions_df['Payment Method'].value_counts().idxmax(), payment_icon["default"])
                                                    )
                                                ],
                                            )
                                        ],
                                    ),
                                    html.P(children=[f"{transactions_df['Payment Method'].value_counts().idxmax()}"]),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            html.Div(
                className="mb-4 rounded-lg p-6 text-center shadow-lg",
                children=[
                    html.H3(
                        className="mb-4 text-4xl font-semibold",
                        children=["Propinas del periodo"],
                    ),
                    dcc.Graph(figure=fig),
                ],
            ),
        ])
    except Exception as e:
        print(e)
        return html.Div(className="text-center", 
                        children=[
                            html.P(
                                className="font-semibold text-red-600",
                                children="Ocurrió un error al buscar los detalles del restaurante.")
                        ])
import base64
import dash
import dash_svg
import io
import requests
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px
from dash import html, dcc, callback, Input, Output, State

dash.register_page(__name__,
                   path="/predicciones",
                   name="Predicción",
                   title="Predicción de restaurantes")

backend_url = "http://localhost:8000"

def get_food_types():
    response = requests.get(f"{backend_url}/food_types")
    return response.json()

def get_states():
    response = requests.get(f"{backend_url}/states")
    return response.json()

def get_price_ranges():
    response = requests.get(f"{backend_url}/price_ranges")
    return response.json()

layout = html.Div(
    className="bg-gray-50",
    children=[
        html.Main(
            className="mx-auto min-h-screen max-w-7xl px-4 py-10",
            children=[
                html.Section(
                    className="mb-10 flex flex-col rounded-lg bg-white p-6 text-gray-700 shadow-lg",
                    children=[
                        html.H2(
                            className="mb-4 text-4xl font-semibold",
                            children=["Predicción para un restaurante"],
                        ),
                        html.Div(
                            className="space-y-6",
                            children=[
                                html.Div(
                                    children=[
                                        html.Label(
                                            className="block text-lg font-medium text-gray-700",
                                            children=["Tipo de comida"],
                                        ),
                                        dcc.Dropdown(
                                            id="food_type",
                                            options=[x["Food Type"] for x in get_food_types()],
                                            className="mt-2 w-full rounded-md border border-gray-300 p-3 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"),
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        html.Label(
                                            className="block text-lg font-medium text-gray-700",
                                            children=["Área de fumadores"],
                                        ),
                                        dcc.RadioItems(
                                            id="smoking_area",
                                            options=[
                                                {"label": "Sí", "value": "Yes"},
                                                {"label": "No", "value": "No"},
                                            ],
                                            inline=True,
                                            inputClassName="focus:ring-blue-500 text-blue-600 border-gray-300 mr-2",
                                            labelClassName="ml-2 text-gray-700",
                                        )
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        html.Label(
                                            className="block text-lg font-medium text-gray-700",
                                            children=["Estado"],
                                        ),
                                        dcc.Dropdown(
                                            id="state",
                                            options=[x["State"] for x in get_states()],
                                            className="mt-2 w-full rounded-md border border-gray-300 p-3 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"),
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        html.Label(
                                            className="block text-lg font-medium text-gray-700",
                                            children=["Ciudad"],
                                        ),
                                        dcc.Input(
                                            id="city",
                                            type="text",
                                            className="mt-2 w-full rounded-md border border-gray-300 p-3 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                                        )
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        html.Label(
                                            className="block text-lg font-medium text-gray-700",
                                            children=["Rango de precio"],
                                        ),
                                        dcc.Dropdown(
                                            id="price_range",
                                            options=[x["Price Range"] for x in get_price_ranges()],
                                            className="mt-2 w-full rounded-md border border-gray-300 p-3 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"),
                                    ]
                                ),
                                html.Div(
                                    className="flex justify-center",
                                    children=[
                                        html.Button(
                                            id="submit-single-prediction",
                                            className="inline-block rounded-lg bg-gradient-to-br from-teal-400 to-blue-500 px-6 py-3 font-semibold text-white shadow-lg hover:from-pink-300 hover:to-orange-600",
                                            children=["Enviar"],
                                        )
                                    ],
                                ),
                            ],
                        ),
                        dcc.Loading(
                            id="loading-single-prediction",
                            children=[html.Div(id="single-prediction-result")],
                        )
                    ],
                ),
                html.Section(
                    className="mb-10 flex flex-col rounded-lg bg-white p-6 text-gray-700 shadow-lg",
                    children=[
                        html.H2(
                            className="mb-4 text-4xl font-semibold",
                            children=["Predicción usando un archivo"],
                        ),
                        html.P(
                            className="mb-4 text-lg",
                            children=[
                                "Subir un archivo csv con los campos:",
                                html.Span(
                                    className="font-semibold text-sky-500",
                                    children=[
                                        "Food Type, Smoker Area, State, City, Price Range"
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="flex flex-col space-y-6",
                            children=[
                                html.Div(
                                    className="flex flex-col md:flex-row space-y-6 space-x-4 md:space-y-0 justify-between items-center",
                                    children=[
                                        dcc.Upload(
                                            id="select-file",
                                            accept=".csv",
                                            multiple=False,
                                            children=[
                                                html.Button(
                                                    className="inline-block rounded-lg bg-blue-500 hover:bg-blue-600 px-6 py-3 font-semibold text-white shadow-lg hover:from-pink-300 hover:to-orange-600",
                                                    children=["Seleccionar archivo"],
                                                    )
                                                ],
                                            ),
                                        html.Div(
                                            id="file-name",
                                            className="flex-1 text-lg font-semibold border-dashed border-2 border-gray-300 rounded-md p-3 shadow-sm",
                                            ),
                                        ],
                                    ),
                                html.Div(
                                    className="flex justify-center",
                                    children=[
                                        html.Button(
                                            id="submit-file-prediction",
                                            className="inline-block rounded-lg bg-gradient-to-br from-teal-400 to-blue-500 px-6 py-3 font-semibold text-white shadow-lg hover:from-pink-300 hover:to-orange-600",
                                            children=["Enviar"],
                                            )
                                        ],
                                    ),
                                dcc.Loading(
                                    id="loading-file-prediction",
                                    children=[
                                        html.Div(id="file-prediction-result")
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            )
        ],
    )

@callback(
    Output("single-prediction-result", "children"),
    Input("submit-single-prediction", "n_clicks"),
    State("food_type", "value"),
    State("smoking_area", "value"),
    State("state", "value"),
    State("city", "value"),
    State("price_range", "value"),
)
def submit_single_prediction(n_clicks, food_type, smoking_area, state, city, price_range):
    if n_clicks is None:
        return None
    data = {
        "food_type": food_type,
        "smoking_area": smoking_area,
        "state": state,
        "city": city,
        "price_range": price_range,
    }
    try:
        response = requests.post(f"{backend_url}/predict", json=data)
        json_response = response.json()
        svg = {
            "Good": "M9 12.75 11.25 15 15 9.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z",
            "Bad": "m9.75 9.75 4.5 4.5m0-4.5-4.5 4.5M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"
        }
        return html.Div(
            className="mt-4 text-center",
            children=[
                html.H3(className="text-2xl font-semibold", children=["Resultados de la predicción:"]),
                html.P(
                    className="text-lg font-semibold",
                    children=[f"Propinas mensuales promedio: ${json_response["monthly_tip_average"]:,.2f}"],
                ),
                html.P(
                    className=f"text-lg font-semibold",
                    children=[
                        "Classificación: ",
                        html.Span(
                            className=f"{"text-red-500" if json_response["classification"] == "Bad" else "text-green-500"}",
                            children=[
                                f"{json_response["classification"]}",
                                dash_svg.Svg(
                                    xmlns="http://www.w3.org/2000/svg",
                                    fill="none",
                                    viewBox="0 0 24 24",
                                    stroke="currentColor",
                                    className=f"inline h-6 w-6",
                                    children=[
                                        dash_svg.Path(
                                            strokeLinecap="round",
                                            strokeLinejoin="round",
                                            d=svg[json_response["classification"]],
                                            )
                                        ],
                                    ),
                                ]
                            ),
                        ],
                    )
                ],
            )
    except Exception as e:
        return html.P(className="text-lg text-red-500", children=[f"Error: {e}"])
    
@callback(
    Output("file-name", "children"),
    Input("select-file", "filename"),
)
def update_file_name(filename):
    if filename is None:
        return "Seleccione un archivo"
    return f"Archivo seleccionado: {filename}"

@callback(
    Output("file-prediction-result", "children"),
    Input("submit-file-prediction", "n_clicks"),
    State("select-file", "contents"),
    State("select-file", "filename"),
)
def submit_file_prediction(n_clicks, contents, filename):
    if n_clicks is None:
        return None
    if contents is None:
        return html.P(className="text-lg text-red-500", children=["Debe seleccionar un archivo csv"])
    content_type, content_string = contents.split(",")
    decoded = base64.b64decode(content_string)
    files = {
        "file": (filename, io.BytesIO(decoded), "text/csv")
    }
    try:
        response = requests.post(f"{backend_url}/predict_file", files=files)
        json_response = response.json()
        predictions_df = pd.DataFrame(json_response)
        classification_pie = px.pie(predictions_df, names="Classification")
        food_type_monthly_tip = predictions_df.groupby("Food Type")["Monthly Tip Average"].mean().reset_index()
        food_type_funnel = px.funnel(food_type_monthly_tip, x="Monthly Tip Average", y="Food Type")
        price_range_monthly_tip = predictions_df.groupby("Price Range")["Monthly Tip Average"].mean().reset_index()
        price_range_bar = px.bar(price_range_monthly_tip, x="Price Range", y="Monthly Tip Average")
        return html.Div(
            className="flex flex-col space-y-6",
            children=[
                html.H3(className="text-2xl font-semibold", children=["Resultados de la predicción:"]),
                dag.AgGrid(
                    id="predictions-table",
                    rowData=predictions_df.to_dict("records"),
                    columnDefs=[{"field": col, "sortable": True, "filter": True } for col in predictions_df.columns],
                    columnSize="responsiveSizeToFit",
                    dashGridOptions={
                        "pagination": True,
                        "paginationPageSize": 20,
                        },
                    csvExportParams={"fileName": "predictions.csv"},
                    ),
                html.Div(
                    className="flex justify-center",
                    children=[
                        html.Button(
                            id="download-predictions",
                            className="inline-block rounded-lg bg-gradient-to-br from-teal-400 to-blue-500 px-6 py-3 font-semibold text-white shadow-lg hover:from-pink-300 hover:to-orange-600",
                            children=["Descargar resultados"],
                            ),
                        ]
                    ),
                html.H3(className="text-2xl font-semibold", children=["Distribución de clasificaciones"]),
                dcc.Graph(figure=classification_pie),
                html.H3(className="text-2xl font-semibold", children=["Propinas promedio por tipo de comida"]),
                dcc.Graph(figure=food_type_funnel),
                html.H3(className="text-2xl font-semibold", children=["Propinas promedio por rango de precio"]),
                dcc.Graph(figure=price_range_bar),
                ]
            )
    except Exception as e:
        return html.P(className="text-lg text-red-500", children=[f"Error: {e}"])

@callback(
    Output("predictions-table", "exportDataAsCsv"),
    Input("download-predictions", "n_clicks"),
    prevent_initial_call=True,
)
def download_predictions(n_clicks):
    if n_clicks:
        return True
    return False
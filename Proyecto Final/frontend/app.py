import dash
from dash import html, dcc


external_stylesheets = []
external_scripts = [
    {"src": "https://cdn.tailwindcss.com"}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, external_scripts=external_scripts, use_pages=True)

nav = html.Nav(
    className="flex md:flex-row flex-col justify-between items-center bg-gradient-to-b from-cyan-500 to-blue-600 px-6 py-8",
    children=[
        html.Div(
            className="flex",
            children=[
                dcc.Link(
                    href="/",
                    children=[
                        html.Img(
                            className="w-52",
                            src=dash.get_asset_url("images/logo.png"),
                            alt="Logo de TipOn",
                        )
                    ],
                )
            ],
        ),
        html.Div(
            className="flex space-x-4 font-semibold text-white text-xl",
            children=[
                dcc.Link(
                    href="/",
                    className="hover:text-blue-200 hover:underline",
                    children=["Inicio"],
                ),
                dcc.Link(
                    href="/negocios",
                    className="hover:text-blue-200 hover:underline",
                    children=["Negocios"],
                ),
                dcc.Link(
                    href="/tableros",
                    className="hover:text-blue-200 hover:underline",
                    children=["Tableros"],
                ),
                dcc.Link(
                    href="/predicción",
                    className="hover:text-blue-200 hover:underline",
                    children=["Predicción"],
                ),
            ],
        ),
    ],
)

footer = html.Footer(
    className="bg-gray-600 py-10 text-center text-white md:text-lg",
    children=[html.P(children=["© 2024 TipOn. Todos los derechos reservados."])],
)

app.layout = html.Div(children=[
    nav,
    dash.page_container,
    footer
])

if __name__ == "__main__":
    app.run(debug=True)
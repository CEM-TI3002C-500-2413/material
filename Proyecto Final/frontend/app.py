import dash
from dash import html


external_stylesheets = []
external_scripts = [
    {"src": "https://cdn.tailwindcss.com"}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, external_scripts=external_scripts, use_pages=True)

nav = html.Nav()

footer = html.Footer()

app.layout = html.Div(children=[
    nav,
    dash.page_container,
    footer
])

if __name__ == "__main__":
    app.run(debug=True)
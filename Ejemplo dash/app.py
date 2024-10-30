from dash import Dash, html, dash_table
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

def load_data(file):
    return pd.read_csv(file)

df = load_data("tips.csv")

external_stylesheets = []
external_scripts = [
    {"src": "https://cdn.tailwindcss.com"}
]

app = Dash(__name__, external_stylesheets=external_stylesheets, external_scripts=external_scripts)

# [
#     {"field": "NombreColumna", "sortable": True, "filter": True}
# ]
app.layout = html.Div(className="bg-gray-50", children=[
    html.Main(className="mx-auto px-4 py-10 max-w-7xl min-h-screen",
              children=[
                  html.H1(className="text-6xl font-bold mb-4", children="Mi primer sitio en Dash"),
                  dash_table.DataTable(data=df.to_dict(orient="records"), page_size=10),
                  dag.AgGrid(rowData=df.to_dict(orient="records"),
                             columnDefs=[{"field": col, "sortable": True, "filter": True} for col in df.columns],
                             columnSize="responsiveSizeToFit",
                             dashGridOptions={"pagination": True, "paginationPageSize": 10})
                  ])
])

if __name__ == "__main__":
    app.run_server(debug=True)
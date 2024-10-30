from dash import Dash, html, dash_table, dcc, callback, Input, Output, State
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

def load_data(file):
    df = pd.read_csv(file)
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    return df

def get_scatter1(df):
    fig = px.scatter(df, x="Total", y="Tip", color="User", size="Tip", labels={"Tip": "Propina", "Total": "Total de la cuenta"})
    fig.update_layout(
        xaxis = {
            "tickmode": "linear",
            "tick0": 40,
            "dtick": 10
        }
    )
    return fig

def get_scatter2(df):
    fig = px.scatter(df, x="Total", y="Tip", color="User", size="Tip", labels={"Tip": "Propina", "Total": "Total de la cuenta"})
    fig.update_layout(
        xaxis = {
            "title": "¿Qué tan cara fue la cuenta?",
            "tickmode": "array",
            "tickvals": [40,110,170,230],
            "ticktext": [
                "Muy barata",
                "Barata",
                "Cara",
                "Muy cara"
            ]
        }
    )
    return fig

def get_bar(df):
    df_user_tip = df.groupby(df["Timestamp"].dt.floor("d"))["Tip"].sum().reset_index()
    # Agregar color para dividir la barra en subsecciones (barras apiladas)
    # Agregar barmode="group" para crear grupos de comparación
    fig = px.bar(df_user_tip, x="Timestamp", y="Tip")
    return fig

def get_line(df):
    df_user_tip = df.groupby(df["Timestamp"].dt.floor("d"))["Tip"].sum().reset_index()
    fig = px.line(df_user_tip, x="Timestamp", y="Tip")
    return fig

def get_pie(df):
    fig = px.pie(df, names="User", values="Tip", hole=0.5)
    return fig

def get_boxplot(df):
    fig = px.box(df, y="Tip")
    return fig

def get_violin(df):
    fig = px.violin(df, y="Tip")
    # color -> Nos muestra un violin por cada valor de la columna color
    return fig

df = load_data("tips.csv")
scatter1 = get_scatter1(df)
scatter2 = get_scatter2(df)
bar = get_bar(df)
line = get_line(df)
pie = get_pie(df)
boxplot = get_boxplot(df)
violin = get_violin(df)

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
                             dashGridOptions={"pagination": True, "paginationPageSize": 10}),
                  dcc.Graph(figure=scatter1),
                  dcc.Graph(figure=scatter2),
                  dcc.Graph(figure=bar),
                  dcc.Graph(figure=line),
                  dcc.Graph(figure=pie),
                  dcc.Graph(figure=boxplot),
                  dcc.Graph(figure=violin),
                  html.H2(className="text-4xl font-semibold mb-4", children="Checklist"),
                  dcc.Checklist(id="checklist1", options=[
                    #   {"label": "Texto que se muestra", "value": "Valor que lee Python"}
                    {"label": "Primer elemento", "value": "Uno"},
                    {"label": "Segundo elemento", "value": "Dos"},
                    {"label": "Tercer elemento", "value": "Tres"},
                  ]),
                  html.H2(className="text-4xl font-semibold mb-4", children="Usuarios registrados"),
                #   dcc.Checklist(id="UsersChecklist", 
                #                 options=[{"label": x, "value": x} for x in df["User"].unique()])
                #   ])
                  dcc.Checklist(id="UsersChecklist", 
                                options=df["User"].unique(),
                                value=df["User"].unique(),
                                inline=True,
                                className="mr-4"),
                  html.Div(id="gráfica por usuario")
                  ]),
])

@callback(
    Output("gráfica por usuario", "children"),
    Input("UsersChecklist", "value")
)
def get_users_bar_chart(user_list):
    df = load_data("tips.csv")
    df = df[df["User"].isin(user_list)].groupby("User")["Tip"].sum().reset_index()
    fig = px.bar(df, x="User", y="Tip")
    return [
        html.P(children=f"Selected users: {user_list}"),
        dcc.Graph(figure=fig)
    ]

if __name__ == "__main__":
    app.run_server(debug=True)
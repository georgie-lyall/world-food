# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import dash_leaflet as dl
import dash_leaflet.express as dlx
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# map_fig = go.Figure(go.Scattergeo())
# map_fig.update_geos(
#     visible=True, 
#     resolution=50,
#     showcountries=True,
# )
# map_fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})

map_df = px.data.gapminder().query("year==2007")
map_df = map_df[['country', 'continent', 'iso_alpha', 'iso_num']]
map_df['completed'] = 0
map_fig = px.choropleth(map_df, 
                    locations="iso_alpha",
                    color="completed",
                    featureidkey="properties.completed",
                    hover_name="country",)

map_card = dbc.Card(
    dbc.CardBody(
        [
            dcc.Graph(figure=map_fig)
        ]
    )
)

container = [
    html.H1("Eat Around the World"),
    html.Div(
        children='Pick a country.'),
    html.Hr(),
    dbc.Row([dbc.Col(map_card)]),
]

app.layout = dbc.Container(container)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
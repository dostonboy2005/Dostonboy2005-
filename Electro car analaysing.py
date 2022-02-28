import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px #(need to pip install plotly.express == 4.4.1)

df = pd.read_csv("ElectricCarData_Clean.csv") #data recieved from kaggle(https://www.kaggle.com/geoffnel/evs-one-electric-vehicle-dataset/version/1)
print(df.head())

app = dash.Dash(__name__)

#____________________________________________________________________
app.layout = html.Div([
    html.Div([
        html.Label(['Electric car price analysis']),
        dcc.Dropdown(
            id='my_dropdown',
            options=[
                {'label': 'Brand', 'value': 'Brand'},
               # {'label': 'Model', 'value': 'Model'},
                {'label': 'Seats', 'value': 'Seats'},
                #{'label': 'Price', 'value': 'PriceEuro'}
            ],
            value='Brand',
            multi=False,
            clearable=False,
            style={"width":"50%"}
        ),

    ]),


    ]),

html.Div([
        dcc.Graph(id='the_graph', figure={}),
         ]),
# Callback ___________________________________________________
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)
def update_graph(my_dropdown):
    dff = df #copy dataframe
    piechart=px.pie(
        data_frame=dff,
        names=my_dropdown,
        hole=0,
        #min=50000,
        #max=15000
    )
    return (piechart)


if __name__ == '__main__':
    app.run_server(debug=True)


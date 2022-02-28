import dash
from dash import dcc
from dash import html
import pandas as pd
from dash.dependencies import Output, Input
import plotly.express as px

df = pd.read_csv('uzb_admpop_adm1.csv')
# print(df[:5])
# print(df.ADM1_EN.nunique())
# print(df.ADM1_EN.unique())

# Data visualization with plotly
# fig_pie = px.pie(data_frame=df, names='ADM1_EN', values='Total_pop')
    # fig_pie = px.pie(data_frame=df, names='ADM1_EN', values='Male_pop')
    # fig_pie.show()

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Uzbekistan population analysis"),
    dcc.Dropdown(
        id='my_dropdown',
        options=[
            {'label': 'Total population', 'value': 'Total_pop'},
            {'label': 'Male population', 'value': 'Male_pop'},
            {'label': 'Female population', 'value': 'Female_pop'}
        ],
        value='Total_pop',
        clearable=False,
        multi=False,

    ),
    html.Div([
        dcc.Graph(id='my_Graph')
    ]),

])

@app.callback(
    Output(component_id='my_Graph', component_property='fig_pie'),
    Input(component_id='my_dropdown',component_property='value')
)

def update_graph(my_dropdown):
    # print(value_ADM1_EN)
    dff = df
    fig_pie = px.pie(
        data_frame=dff,
        names=my_dropdown,
        hole=.3,
    )
    return (fig_pie)



if __name__=='__main__':
    app.run_server()




# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 16:57:20 2021

@author: viive
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:50:44 2021

@author: viive
"""

import pandas as pd
import datetime as dt
import dash        
from dash import dcc as dcc
from dash import html as html
from dash.dependencies import Input, Output
from dash import dash_table as dt

import plotly
import plotly.express as px

df = pd.read_csv("flip_mob.csv")


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#------------------------------


app = dash.Dash(__name__)

#-------------------------------------------------------------------------------------

app.layout = html.Div([html.H1('Flipkart Mobile Sales Dashboard ', 
                               style = {'fontSize': 70, 'textAlign' : 'center', 'background-color': 'SteelBlue','color' : 'white'}),
                       html.P("⦿ Flipkart is India's Second largest E-Commerce firms ",
                              style = {'fontSize': 15, 'textAlign' : 'center', "font-weight": "bold",'color' : 'Teal'}),
                       html.P("⦿ E-Sales of Mobile Devices has increased by 850% YoY ",
                              style = {'fontSize': 15, 'textAlign' : 'center', "font-weight": "bold",'color' : 'Teal'}),
                       html.P("⦿ The Dashboard aims to generate effective insights of mobile sales based on device parameters ",
                              style = {'fontSize': 15, 'textAlign' : 'center', "font-weight": "bold",'color' : 'Teal'}),
                       
                       html.Div([
    html.P("Select Device Parameter",
           style = {'fontSize': 20, 'textAlign' : 'left', "font-weight": "bold",'color' : 'Teal'}),
    dcc.Dropdown(
        id='names',
        value='brand',
        options=[{'value': x, 'label': x}
                 for x in ['brand', 'base_color', 'processor']],
        clearable=False
    ),
    html.P("Select Sales Parameter",
           style = {'fontSize': 20, 'textAlign' : 'left', "font-weight": "bold",'color' : 'Teal'}),
    dcc.Dropdown(
        id='values',
        value='sales',
        options=[{'value': x, 'label': x}
                 for x in ['sales', 'sales_price']],
        clearable=False
    ),
    dcc.Graph(id="pie-chart"),
    
   html.Div([
        html.H3('Search Results',
                style = {'fontSize': 30, 'textAlign' : 'left', "font-weight": "bold",'color' : 'Teal'}),
        
        html.H5('**Scroll to see complete table summary',
                style = {'fontSize': 15, 'textAlign' : 'left', "font-weight": "bold",'color' : 'Teal'}),
        
                     dt.DataTable(id = 'my_datatable',
                     columns =[{'id': c, 'name':c} for c in ('brand', 'base_color', 'processor','sales', 'sales_price')],
                     virtualization = True,
                     page_action = 'native',
                     page_size=150,
                     editable=True,
                     style_table={'height': '300px', 'overflowY': 'auto'},
                     style_header={'backgroundColor': 'Teal', 'font-weight': "bold",'color': 'white'},
                     style_cell={
                         'backgroundColor': 'white',
                         'color': 'Teal'
                    }),
              html.H5('Reference',
                      style={'fontSize':25, 'textAlign':'center', 'color': 'Teal'}
                      ),
    html.Div([
           html.A("Data Source.",
               href = 'https://www.kaggle.com/shubhambathwal/flipkart-mobile-dataset',
               style={'fontSize':15, 'textAlign':'center', 'color': 'Teal'}),
           html.Br(),
           html.Br(), 
           html.A(" Pie Chart.",
           href = "https://plotly.com/python/pie-charts/",
           style={'fontSize':15, 'textAlign':'center', 'color': 'Teal'}),
           html.Br(),
           html.A(" Data Table.",
           href = "https://dash.plotly.com/datatable",
           style={'fontSize':15, 'textAlign':'center', 'color': 'Teal'}),
           html.Br(),
           html.A(" Color.",
           href = "w3schools.com/colors/colors_names.asp",
           style={'fontSize':15, 'textAlign':'center', 'color': 'Teal'})
       ])
    
   
      ])
   
 
])
     ])


server = app.server


@app.callback(
    Output("pie-chart", "figure"),
    [Input("names", "value"),
     Input("values", "value")])

def generate_chart(names, values):

    fig = px.pie(df, values=values, names=names)
    return fig


@app.callback(
    Output('my_datatable', 'data'),
    [Input('names', 'value'),
    Input('values', 'value')]

)

def display_table(names, values):
    
    table=df[[names,values]]

    return table.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)


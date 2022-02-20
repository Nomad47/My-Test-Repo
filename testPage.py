'''
    # ~~~ @author: alect ~~~ #
    Run this app with `python app.py` and visit
    http://127.0.0.1:8050/ in your web browser.
'''

# --- System utils --- #
import sys
import os 
# -------------------- #



# --- Dash Application Imports --- #
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
# -------------------------------- #

# --- Plotting utils --- #
import plotly.express as px
import plotly.graph_objects as go
# ---------------------- #

# --- Pandas utils --- #
import pandas as pd
# -------------------- #

app = dash.Dash()

# --- Import and clean data --- #
df = px.data.stocks()
# ----------------------------- # 

markdownText = \
'''
    ### This is a sample markdown...

    Dash apps can be written in Markdown.
    Dash uses the [CommonMark](http://commonmark.org/)
    specification of Markdown.
    Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
    `if this is your` first introduction to Markdown!
'''

labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500, 2500, 1053, 500]

dropdown1 = dcc.Dropdown(id='dropdown',
                         options = [
                             {'label':'Google', 'value':'GOOG' },
                             {'label': 'Apple', 'value':'AAPL'},
                             {'label': 'Amazon', 'value':'AMZN'},
                             ],
                         value = 'GOOG'
                         )

# -------------------------------------------------------------------------- #
# Generate Application Layout
app.layout = html.Div(id = 'parent',
                      children = [
                          # --- Set Header 1 HTML Layout --- #
                          html.H1(id = 'H1', 
                                  children ='ARTTViz - Another Redundant \
                                             Tensor Toolbox Vizualizer', 
                                  style = {'textAlign':'center', 
                                           'marginTop':40, 
                                           'marginBottom':40
                                           }
                                  ),
                          
                          # --- Create dropdown-menu --- #
                          dropdown1,
                          # ---------------------------- #
                          
                          # --- Create bar chart --- #
                          html.Br(),    
                          dcc.Graph(id='bar_plot'),
                          # ------------------------ #
                          
                          # --- Create pie-charts & inline --- #
                          html.Div(dcc.Graph(id='pie_plot'), 
                                   style={'width':'49%', 'display':'inline-block'}
                                   ),
                          
                          html.Div(dcc.Graph(id='pie_plot_2'), 
                                   style={'width':'49%', 'display':'inline-block'}
                                   ),
                          # --------------------------------------- #
                          
                          # --- Create text markdown column --- #
                          html.Br(),
                          dcc.Markdown(children=markdownText)
                          # ----------------------------------- #
                      ])
# -------------------------------------------------------------------------- #

# -------------------------------------------------------------------------- #
# Line Graph Application Callback    
@app.callback(Output(component_id='bar_plot', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value')])
def lineGraphUpdate(dropdown_value):
    #print(dropdown_value)
    
    # --- Perform classification as needed --- #
    #performSupervisedClassification()
    # ---------------------------------------- #
    
    # --- Update the line chart --- #
    lineFig = go.Figure(data = \
                        [go.Scatter(x = df['date'], 
                                    y = df[('{}').format(dropdown_value)],
                                    line = dict(color='firebrick', width = 4)
                                    )])
    # ----------------------------- #
        
    lineFig.update_layout(title = 'Stock prices over time',
                          xaxis_title = 'Dates',
                          yaxis_title = 'Prices'
                          )
    
    return lineFig 

# -------------------------------------------------------------------------- #
# Pie Chart Application Callback  
@app.callback(Output(component_id='pie_plot', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value')])
def pieChartUpdate(dropdown_value):
     #print(dropdown_value)
    
    pieFig = go.Figure(data = [go.Pie(labels = labels, 
                                      values = values, 
                                      hole = 0.5
                                      )])
    
    pieFig.update_layout(title='This is a pie chart')
    
    return pieFig
# -------------------------------------------------------------------------- #

# -------------------------------------------------------------------------- #
# Pie Chart 2 Application Callback  
@app.callback(Output(component_id='pie_plot_2', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value')])
def pieChartUpdate2(dropdown_value):
     #print(dropdown_value)
    
    pieFig = go.Figure(data = [go.Pie(labels = labels, 
                                      values = values, 
                                      hole = 0.5
                                      )])
    
    pieFig.update_layout(title='This is a pie chart')
    
    return pieFig
# -------------------------------------------------------------------------- #

if __name__ == '__main__': 
    app.run_server() 
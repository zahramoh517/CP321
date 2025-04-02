#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd
import numpy as np
import dash
from dash import dcc, html
import plotly.express as px


# In[44]:


data = {
    'Year': [2018, 2014, 2010, 2006, 2002, 1998, 1994, 1990, 1986, 1982],
    'Winner': ['France', 'Germany', 'Spain', 'Italy', 'Brazil', 'France', 'Brazil', 'Germany', 'Argentina', 'Italy'],
    'Runner-up': ['Croatia', 'Argentina', 'Netherlands', 'France', 'Germany', 'Brazil', 'Italy', 'Argentina', 'Germany', 'West Germany']
}


# In[45]:


df = pd.DataFrame(data)

df.replace({'Winner': {'West Germany': 'Germany'}, 'Runner-up': {'West Germany': 'Germany'}}, inplace=True)

wins = df['Winner'].value_counts().reset_index()
wins.columns = ['Country', 'Wins']
wins['Wins'] = wins['Wins'].astype(int)  


# In[46]:


fig = px.choropleth(
    wins,
    locations='Country',
    locationmode='country names',
    color='Wins',
    title='FIFA World Cup Winners',
    color_continuous_scale='Plasma'
)


# In[47]:


fig = px.choropleth(
    wins,
    locations='Country',
    locationmode='country names',
    color='Wins',
    title='FIFA World Cup Winners',
    color_continuous_scale=[(0, "#f7fbff"), (0.2, "#deebf7"), (0.4, "#9ecae1"), (0.6, "#4292c6"), (0.8, "#2171b5"), (1, "#084594")],
    range_color=[1, wins['Wins'].max()]
)


# In[48]:


# Dash App Layout
app = dash.Dash(__name__)
server = app.server
app.layout = html.Div([
    html.H1("FIFA World Cup Dashboard", style={'textAlign': 'center'}),
    dcc.Graph(id='choropleth', figure=fig),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': c, 'value': c} for c in wins['Country']],
        placeholder="Select a country"
    ),
    html.Div(id='country-output'),
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': y, 'value': y} for y in df['Year']],
        placeholder="Select a year"
    ),
    html.Div(id='year-output')
])


# In[49]:


# callbacks
@app.callback(
    dash.Output('country-output', 'children'),
    dash.Input('country-dropdown', 'value')
)
def update_country(selected_country):
    if selected_country:
        wins_count = wins[wins['Country'] == selected_country]['Wins'].values[0]
        return f"{selected_country} has won the World Cup {wins_count} times."
    return ""

@app.callback(
    dash.Output('year-output', 'children'),
    dash.Input('year-dropdown', 'value')
)
def update_year(selected_year):
    if selected_year:
        row = df[df['Year'] == selected_year]
        return f"In {selected_year}, {row['Winner'].values[0]} won, and {row['Runner-up'].values[0]} was the runner-up."
    return ""

if __name__ == '__main__':
    app.run(debug=True)



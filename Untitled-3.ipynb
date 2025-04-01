{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "7fabf9e2-4c06-4e8b-aa27-5a6d2dc9e07a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import dash\n",
    "from dash import dcc, html\n",
    "import plotly.express as px"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "12c54a63-4eaa-4106-96dc-3fb2b233a481",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = {\n",
    "    'Year': [2018, 2014, 2010, 2006, 2002, 1998, 1994, 1990, 1986, 1982],\n",
    "    'Winner': ['France', 'Germany', 'Spain', 'Italy', 'Brazil', 'France', 'Brazil', 'Germany', 'Argentina', 'Italy'],\n",
    "    'Runner-up': ['Croatia', 'Argentina', 'Netherlands', 'France', 'Germany', 'Brazil', 'Italy', 'Argentina', 'Germany', 'West Germany']\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "b042229b-3a2c-4a66-bfd9-b36e437100ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(data)\n",
    "\n",
    "df.replace({'Winner': {'West Germany': 'Germany'}, 'Runner-up': {'West Germany': 'Germany'}}, inplace=True)\n",
    "\n",
    "wins = df['Winner'].value_counts().reset_index()\n",
    "wins.columns = ['Country', 'Wins']\n",
    "wins['Wins'] = wins['Wins'].astype(int)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "92ab64e8-1f24-4c7a-b36c-fbe8056de280",
   "metadata": {},
   "outputs": [],
   "source": [
    "fig = px.choropleth(\n",
    "    wins,\n",
    "    locations='Country',\n",
    "    locationmode='country names',\n",
    "    color='Wins',\n",
    "    title='FIFA World Cup Winners',\n",
    "    color_continuous_scale='Plasma'\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "146e0ef3-945c-4618-9c0d-bcb04e42219c",
   "metadata": {},
   "outputs": [],
   "source": [
    "fig = px.choropleth(\n",
    "    wins,\n",
    "    locations='Country',\n",
    "    locationmode='country names',\n",
    "    color='Wins',\n",
    "    title='FIFA World Cup Winners',\n",
    "    color_continuous_scale=[(0, \"#f7fbff\"), (0.2, \"#deebf7\"), (0.4, \"#9ecae1\"), (0.6, \"#4292c6\"), (0.8, \"#2171b5\"), (1, \"#084594\")],\n",
    "    range_color=[1, wins['Wins'].max()]\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "915cd4fb-f81f-4dbf-827e-575fcc506988",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dash App Layout\n",
    "app = dash.Dash(__name__)\n",
    "app.layout = html.Div([\n",
    "    html.H1(\"FIFA World Cup Dashboard\", style={'textAlign': 'center'}),\n",
    "    dcc.Graph(id='choropleth', figure=fig),\n",
    "    dcc.Dropdown(\n",
    "        id='country-dropdown',\n",
    "        options=[{'label': c, 'value': c} for c in wins['Country']],\n",
    "        placeholder=\"Select a country\"\n",
    "    ),\n",
    "    html.Div(id='country-output'),\n",
    "    dcc.Dropdown(\n",
    "        id='year-dropdown',\n",
    "        options=[{'label': y, 'value': y} for y in df['Year']],\n",
    "        placeholder=\"Select a year\"\n",
    "    ),\n",
    "    html.Div(id='year-output')\n",
    "])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "a049ab36-33b6-4cea-b484-1488f43f6b52",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:8050/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x15f99fe00>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# callbacks\n",
    "@app.callback(\n",
    "    dash.Output('country-output', 'children'),\n",
    "    dash.Input('country-dropdown', 'value')\n",
    ")\n",
    "def update_country(selected_country):\n",
    "    if selected_country:\n",
    "        wins_count = wins[wins['Country'] == selected_country]['Wins'].values[0]\n",
    "        return f\"{selected_country} has won the World Cup {wins_count} times.\"\n",
    "    return \"\"\n",
    "\n",
    "@app.callback(\n",
    "    dash.Output('year-output', 'children'),\n",
    "    dash.Input('year-dropdown', 'value')\n",
    ")\n",
    "def update_year(selected_year):\n",
    "    if selected_year:\n",
    "        row = df[df['Year'] == selected_year]\n",
    "        return f\"In {selected_year}, {row['Winner'].values[0]} won, and {row['Runner-up'].values[0]} was the runner-up.\"\n",
    "    return \"\"\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

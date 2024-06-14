from fetch import fetch

from dash import Dash, html, dash_table, dcc
import plotly.express as px
import pandas as pd

df = fetch("ship:startrix")

app = Dash()

app.layout = [
    html.Div(children='Data'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(df, x='date'))
]

if __name__ == '__main__':
    app.run(debug=True)

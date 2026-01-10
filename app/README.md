# Dashboard app

This folder will contain the Dash/Plotly app entrypoint and deployment config.

# app/app.py

from dash import Dash, html

app = Dash(**name**)
server = app.server

app.layout = html.Div([
html.H1("GapSight Health"),
html.P("Dashboard coming soon. See live demo link in README.")
])

if **name** == "**main**":
app.run_server(debug=True)

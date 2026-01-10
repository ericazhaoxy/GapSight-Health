from dash import Dash, html

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("GapSight Health"),
    html.P("Dashboard coming soon. See live demo link in README.")
])

if __name__ == "__main__":
    app.run_server(debug=True)
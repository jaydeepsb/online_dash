import time
import dash
from dash import Dash, dcc, html, Input, Output, ctx, State
from dash import dash_table as dt
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

app = Dash(__name__)
server = app.server

# Define the layout of the app
app.layout = html.Div([
    html.H1('Type Alphabets'),
    dcc.Input(id='input', type='text', value=''),
    html.Button('+', id='button-inc', n_clicks=0),
    html.Button('-', id='button-dec', n_clicks=0),
    html.Div(id='output', style={'fontSize': 80}),
])


# Define the callback functions
@app.callback(
    Output('output', 'children'),
    Input('input', 'value'),
    Input('button-inc', 'n_clicks'),
    Input('button-dec', 'n_clicks'),
)
def update_output(input_value, n_clicks_inc, n_clicks_dec):
    # Determine the font size based on the number of clicks
    font_size = 24 + 2 * (n_clicks_inc - n_clicks_dec)
    font_size = max(10, min(font_size, 36))

    # # Determine the text color based on the color that was clicked
    # ctx = dash.callback_context
    # color_id = ctx.triggered[0]['prop_id'].split('.')[0]
    # color = colors.get(color_id, 'black')

    # Return the updated output
    return html.Div(input_value, style={'fontSize': font_size})

if __name__ == "__main__":
    app.run_server(debug=False)

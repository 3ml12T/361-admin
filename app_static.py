import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime as dt
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='mygraph'),
    dcc.Interval(
        id='interval-1-component',
        interval=1 * 1000,  # in milliseconds
        n_intervals=0
    ),
])


@app.callback([Output('mygraph', 'figure'),
               Output('mygraph', 'config')],
              [Input('interval-1-component', 'n_intervals')])
def update_mygraph(n):
    fig = {
        'data': [
            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'}
        ],
        'layout': {
            'title': f'Static Graph Demo: {dt.datetime.now()}'
        }
    }

    config = {'staticPlot': True}

    return fig, config


if __name__ == '__main__':
    app.run_server(debug=True)
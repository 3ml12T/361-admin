import plotly.graph_objects as go
import plotly.express as px
from dash import Dash, dcc, Output, Input, html  

app = Dash(__name__)

# extract data from csv file, save to new variable
csvFile = 'cum_data.csv'
df = px.pd.read_csv(csvFile)

# set graph layout, radio buttons and graph itself
app.layout = html.Div([
    dcc.RadioItems(
        ['All', 'E5-6008', 'SYDE Lounge'], 
        'All',
        inline=True,
        id='location'),
    dcc.Graph(
        id='horizontal-bar-chart',)    
])

@app.callback(
    Output('horizontal-bar-chart', 'figure'),
    Input('location', 'value'))

# update graph based on radio button pressed    
def update_figure(location_value):

    if location_value != 'All':
        filtered_df = df[df["Location"]==location_value]
    else:
        filtered_df = df

# establish formatting configuration: x,y values, colors, and height of graph
    fig = px.bar(filtered_df,
                x='value',
                y='type',
                color='Location',
                # color_discrete_sequence=["goldenrod", "magenta", "blue"],
                color_discrete_map={'E5-6008': '#0041A4','SYDE Lounge': '#3385FF', 'DC Library': '#B3D1FF'},
                orientation='h',
                height=400)
    fig.update_layout(transition_duration=500)

    # name the axes based on csv specifics 
    fig['layout']['xaxis']['title']='Percentage of Time (%)'
    fig['layout']['yaxis']['title']='Light Level (Flux)'

    return fig#, config

if __name__ == '__main__':
    app.run_server(debug=True)
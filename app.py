import plotly.graph_objects as go
import plotly.express as px
from dash import Dash, dcc, Output, Input, html  

app = Dash(__name__)
#fig = go.Figure()
#fig.add_trace(go.Bar(
#    y=['>25', '23-25', '20-22 (ideal)', "17-19", "<17"],
#    x=[5, 15, 25, 17, 12],
#    name='E5-6008',
#    orientation='h',
#    marker=dict(
#        color='rgba(246, 78, 139, 0.6)',
#        line=dict(color='rgba(246, 78, 139, 1.0)', width=2)
#    )
#))
#fig.add_trace(go.Bar(
#    y=['>25', '23-25', '20-22 (ideal)', "17-19", "<17"],
#    x=[10, 11, 15, 7, 2],
#    name='SYDE Lounge',
#    orientation='h',
#    marker=dict(
#        color='rgba(58, 71, 80, 0.6)',
#        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
#    )
#))
#
#fig.update_layout(barmode='stack')
#fig.show()

csvFile = 'cum_data.csv'
df = px.pd.read_csv(csvFile)

#radioButtons = dcc.RadioItems(['All', 'E5-6008', 'SYDE Lounge'], 'All',inline=True)
# graph = dcc.Graph(figure={})
# filtered_df=df[df["Location"] == "E5-6008"]
# fig = px.bar(filtered_df, 
            # x='value', 
            # y='type', 
            # color='Location', 
            # orientation='h',
                # height=400,
                # title="Cumulative Data",
            # )
# fig.show()

app.layout = html.Div([
    dcc.RadioItems(
        ['All', 'E5-6008', 'SYDE Lounge'], 
        'E5-6008',
        inline=True,
        id='location-radioButton'),
    dcc.Graph(
        id='horizontal-bar-chart',)    
])

@app.callback(
    Output('horizontal-bar-chart', 'figure'),
    Input('location-radioButton', 'location'))
def update_figure(selected_location):
    #filtered_df = df[df['Location'] == selected_location]
    print (selected_location)
    print (df)
    #Returns an empty data frame no matter location choice 
    fig = px.bar(filtered_df,
                x='value',
                y='type',
                color='Location',
                orientation='h',
                height=400,
                title='Cumulative Data')
    fig.update_layout(transition_duration=500)
    #config = {'staticPlot': True}

    return fig#, config


if __name__ == '__main__':
    app.run_server(debug=True)
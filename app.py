from dash import Dash, html, dcc
import plotly.graph_objects as go
import pandas as pd
import numpy as np

z = [[.1, .3, .5, .7, .9],
     [1, .8, .6, .4, .2],
     [.2, 0, .5, .7, .9],
     [.9, .8, .4, .2, 0],
     [.3, .4, .5, .7, 1]]

app = Dash(__name__)

image1 = 'assets/floor-plan.jpg'

trace1 = dict(z=np.flipud(z),
              type="heatmap",
              zmin=0.0,
              zmax=1.0,
              colorscale='YlOrRd',
              opacity= 0.5)

source_image_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/FullMoon2010.jpg/800px-FullMoon2010.jpg'

layout = go.Layout(images=[go.layout.Image(source=image1,
                           xref= "x",
                           yref= "y",
                           x= 0,
                           y= 20,
                           sizex= 20,
                           sizey= 40,
                           sizing= "stretch",
                           opacity= 0.5,
                           layer= "below")])

fig = go.Figure(data=[trace1], layout=layout)


app.layout = html.Div([
        html.H1(children='Heatmap', style={'textAlign':'center'}),
        dcc.Graph(id='graph', figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)

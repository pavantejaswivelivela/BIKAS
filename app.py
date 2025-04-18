import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
#import dash_auth # pip install dash-auth

#USERNAME_PASSWORD_PAIRS = [['username','password'], ['Bikasvisual', 'Bikas@Mcgill']]

df = pd.read_csv('xDID.csv')
df1 = pd.read_csv('xDID.csv')

app = dash.Dash(__name__) # Application Name

#auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS)
features = df.columns # only contains columns ['Embodiment Function', 'Biological Feature Characteristic' etc]

color_map = {'Surfaces':'red', 'Cross-sections':'blue', 'Shapes':'black', 'Cellular structures': 'green'}
df_color = df['Domain'].map(color_map)

data1 = [go.Scatter(x = df['Embodiment Function'], 
                   y = df['Biological feature characteristic'], 
                   mode = 'markers',
                   marker = dict(  #markers are dots, squares or any shapes that points the data point
                       size = 12, # size of the marker
                       color = df_color,
                       symbol= 'hexagon', # shape of the marker
                       line = {'width':2} #Width of the line on the marker
                   ))]

layout1 = go.Layout(title='Embodiment Function Vs Biological feature characteristic',
                   xaxis={'title': 'Embodiment Function'},
                   yaxis=dict(title='Biological feature characteristic', color ='black'),
                   hovermode='closest'
                 )
fig1 = go.Figure(data=data1, layout=layout1)

data2 = [go.Scatter(x=df['Embodiment Function'],
                   y = df['Biological Feature'],
                   text = df['Domain'], # displays the name of the Domain when we hoverover the point
                   mode='markers',
                   marker= dict(size =12, color = df_color, symbol ='hexagon', line = {'width':2})
        )]
layout2 = go.Layout(title='Embodiment Function Vs Biological feature', 
                    xaxis={'title': 'Embodiment Function'},
                    yaxis=dict(title='Biological Feature', color ='black'),
                    hovermode='closest')
fig2 = go.Figure(data=data2, layout=layout2)

data3 = [go.Scatter(x=df['Biological Feature'],
                   y = df['Tissues'],
                   text = df['Domain'], # displays the name of the Domain when we hoverover the point
                   mode='markers',
                   marker= dict(size =12, color = df_color, symbol ='hexagon', line = {'width':2})
                   
        )]
layout3 = go.Layout(title='Biological feature Vs. Tissues', 
                    xaxis={'title': 'Biological Feature'},
                    yaxis=dict(title='Tissues', color ='black'),
                    hovermode='closest')
fig3 = go.Figure(data=data3, layout=layout3)

data4 = [go.Scatter(x=df['Biological Feature'],
                   y = df['Domain'],
                   text = df['Biological feature characteristic'], # displays the name of the Domain when we hoverover the point
                   mode='markers',
                   marker= dict(size =12, color = df_color, symbol ='hexagon', line = {'width':2})
                   
        )]
layout4 = go.Layout(title='Biological feature Vs. Domain', 
                    xaxis={'title': 'Biological feature'},
                    yaxis=dict(title ='Domain', color ='black'),
                    hovermode='closest')
fig4 = go.Figure(data=data4, layout=layout4)


df['Domain'].replace(['Surfaces', 'Cross-sections', 'Shapes', 'Cellular Structures'], 
                     [0,1,2,3])
#data5 = [go.Heatmap(x=df['Embodiment Function'], y=df['Biological feature characteristic'], z= df['Domain'].values.tolist(),
        #colorscale='jet')]
#layout5 = go.Layout(title='HeatMap',
                    #xaxis={'title': 'Embodiment Function'},
                    #yaxis=dict(title='Biological feature characteristic', color ='black'))
#fig5 = go.Figure(data=data5, layout=layout5)

app.layout = html.Div([
    html.H1('BIKAS: Bio-inspired Knowledge Acquisition and Simulacrum',
            style={'textAlign':'center','color': 'Black'}),
    html.H3('This is an interactive knowledge database for Multifunctional Bio-inspired Design (MBID) Ideation System', style={'textAlign':'center','color': 'Black'}),
    html.H3('Multifunctional Bio-inspired Design (MBID) is a rapid ideation system developed for the generation of multifunctional bio-inspired designs.', style={'textAlign':'center','color': 'Brown'}),
    html.H3('A brief description about the Multifunctional Bio-inspired design ideation system can be accessed here: https://pavantejaswivelivela.github.io/Multifunctional-BID/', style={'textAlign':'center','color': 'Brown'}),
    html.H3('The following are the interactive knowledge graphs that provides the user with the details of the biological feature, its embodiment function, its corresponding domain and the tissue from which it originates. Users can perform actions such as hovering over, zooming in, and zooming out over the graphs that describe the function, feature, feature characteristics, and respective domains.',
            style={'textAlign':'center','color': 'Brown'}),
    html.H3('Each color of the hexagonal marker describes a domain. The color red represents the biological feature in the surfaces domain, the color blue represents the feature in the cross-sections domain, similarly the color black represents the feature in shapes domain, and the color green represents the feature in the cellular-structures domain',
            style={'textAlign':'center','color': 'Brown'}),
    html.H3('Here is a brief description of terminologies,  (A) Biological features are the morphological and anatomical features observed in plant and animal kingdoms. (B) Biological Feature characteristics describe a feature appearance, apparent form, or physical trait.',
            style={'textAlign':'center','color': 'Brown'}),
    html.H3('More about the Multifunctional Bio-inspired Design (MBID) ideation system can be accessed via https://pavantejaswivelivela.github.io/Multifunctional-BID/', style={'textAlign':'center','color': 'Brown'}),
    html.H3('More about the unique multifunctional bio-inspired conceptual designs can be accessed via https://sites.google.com/view/pavantejaswivelivela', style={'textAlign':'center','color': 'Brown'}),
    html.H3('Publication of BIKAS:  Velivela, P.T. and Zhao, Y.F., 2023. BIKAS: Bio-Inspired Knowledge Acquisition and Simulacrum—A Knowledge Database to Support Multifunctional Design Concept Generation. Data Intelligence, pp.1-28. DOI: https://doi.org/10.1162/dint_a_00240', style={'textAlign':'center','color': 'Brown'}),
    html.Div([dcc.Graph(id='bubble-chart1', figure = fig1)],style = {'width': '100%','display': 'inline-block'}),
    html.Div([dcc.Graph(id='bubble-chart2', figure = fig2)],style = {'width': '100%','display': 'inline-block'}),
    html.Div([dcc.Graph(id='bubble-chart3', figure = fig3)],style = {'width': '100%','display': 'inline-block'}),
    html.Div([dcc.Graph(id='bubble-chart4', figure = fig4)],style = {'width': '100%','display': 'inline-block'}),
    #html.Div([dcc.Graph(id='HeatMap', figure = fig5)],style = {'width': '90%','display': 'inline-block'}),
    html.Div([dcc.Interval(id='interval-component', interval = 5000, n_intervals=0)]),
    html.H4('Corresponding author: Porf. Yaoyao Fiona Zhao, Additive Design and Manufacturing Laboratory (ADML), Department of Mechanical Engineering, McGill University, Montreal, Canada. Email: yaoyao.zhao@mcgill.ca', style={'textAlign':'center','color': 'Black'}),
    html.H4('Author: Pavan Tejaswi Velivela, Email: pavan.velivela@mail.mcgill.ca, pavan.velivela90@gmail.com, portfolio: https://sites.google.com/view/pavantejaswivelivela', style={'textAlign':'center','color': 'Black'}),
    html.H4('© 2025 Pavan Tejaswi Velivela. All rights reserved', style={'textAlign':'center','color': 'Black'}),
    html.H4('The land I work at is situated on the traditional territory of the Kanien’kehà:ka, a place which has long served as a site of meeting and exchange amongst many First Nations including the Kanien’kehá:ka of the Haudenosaunee Confederacy, Huron/Wendat, Abenaki, and Anishinaabeg.',
           style={'textAlign':'center','color': 'Black'})
    #dcc.Graph(id ='feature-graphic'),
     #html.Div([
        #dcc.Dropdown(id ='xaxis_name',
                     #options=[{'label': i, 'value':i} for i in features],
                     #value = 'Embodiment Function')
    #], style = {'width':'48%','display':'inline-block'}),
    #html.Div([
        #dcc.Dropdown(id = 'yaxis_name',
                     #options=[{'label': i, 'value':i} for i in features],
                     #value = 'Domain')
    #], style = {'width':'48%', 'display':'inline-block'})
])

#@app.callback(Output('bubble-chart1', 'bubble-chart2'),
              #[Input('interval-component', 'n_intervals')])

#def update_layout(n):
    #return "{} Page Refereshs".format(n)

#@app.callback(Output('feature-graphic','figure'),
              #[Input('xaxis_name','value'),
               #Input('yaxis_name','value')])

#def update_graph(xaxis_name, yaxis_name):
    #return {'data': [go.Scatter(x=df1[xaxis_name],
                                #y=df1[yaxis_name],
                                #text=df1['Domain'],
                                #mode='markers',
                                #marker= dict(color = df_color))
                            #],
            #'layout':go.Layout( xaxis = {'title':xaxis_name},
                                #yaxis = {'title':yaxis_name})} 

app = app.server

if __name__=='__main__':
    app.run_server()

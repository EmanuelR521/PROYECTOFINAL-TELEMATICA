import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State


app = dash.Dash()

app.layout = html.Div([
    html.H3("Ingresa tus credenciales:"),
    dcc.Input(id="user", type="text", placeholder="Usuario"),
    dcc.Input(id="password", type="text", placeholder="Contraseña"),
    html.Button('Enviar', id='submit-button', n_clicks=0),
    html.Div(id='output')
])

@app.callback(Output('output', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('user', 'value'),
               State('password', 'value')])

def update_output(n_clicks, user, password):
    valido = False
    if user == "a" and password == "a":
      valido = True

    if valido:
      url = "http://34.225.20.33:1001/mostrar_estacionesnivel"
      data = pd.read_json(url,convert_dates='True')

      latr = []
      lonr = []
      zr = []
      for i in range(0,100):
        zr.append(data['datos'][i]['porcentajeNivel'])
        latr.append(data['datos'][i]['coordenadas'][0]['latitud'])
        lonr.append(data['datos'][i]['coordenadas'][0]['longitud'])

      fig = go.Figure(go.Densitymapbox(lat=latr,lon=lonr,z=zr,radius=20, opacity=0.9, zmin=0, zmax = 100))
      fig.update_layout(mapbox_style="stamen-terrain",mapbox_center_lon=-75.589,mapbox_center_lat=6.2429)
      fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

      return html.Div([
                 html.H1("PROYECTO API SIATA"),
                 dcc.Graph(figure=fig)
                 ])
    else:
      if n_clicks > 0:
        return html.Div([
            html.H3('Credenciales incorrectas', style={'color': 'red'})
        ])
app.run_server(host='0.0.0.0',port=1000)


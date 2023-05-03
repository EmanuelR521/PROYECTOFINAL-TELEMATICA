import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

app = dash.Dash()
app.layout = html.Div([
    html.H3("INICIO DE SESION:", style={'color': 'blue'}),
    dcc.Input(id="user", type="text", placeholder="Usuario"),
    dcc.Input(id="password", type="password", placeholder="Contraseña"),
    html.Button('Enviar', id='submit-button', n_clicks=0),
    html.Div(id='output')
])

@app.callback(Output('output', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('user', 'value'),
               State('password', 'value')])
# en la funcion hay varios print que solo sirven para verificar hasta donde esta llegando el codigo
def validarDatos(n_clicks, user, password):
    valido = False
    ArrayUsers = []
    ArrayPasswords = []
    url="http://34.225.20.33:1002/recibir_DB"
    data = pd.read_json(url,convert_dates=True)
    print(type(data))
    for i in range(0,3):
      ArrayUsers.append(data['user'][i])
      ArrayPasswords.append(data['password'][i])
    print(ArrayUsers)
    print(ArrayPasswords)
    for i in range(0,3):
      print("entra al for")
      if ArrayUsers[i] == user and str(ArrayPasswords[i]) == password:
        print("entra al if")
        valido = True
    print (valido)

    if valido:
      url = "http://34.225.20.33:1001/api"
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
                 html.H2("BIENVENIDO AL API DEL SIATA", style ={'color': 'orange' }),
                 dcc.Graph(figure=fig)
                 ])
    else:
      if n_clicks > 0:
        return html.Div([
            html.H2('USUARIO O CONTRASEÑA INCORRECTOS', style={'color': 'red'})
        ])

app.run_server(host='0.0.0.0',port=1000)


import pandas as pd
import plotly.graph_objects as go


import dash
from dash import dcc
from dash import html

url = "http://3.94.4.188:5000/mostrar_estacionesnivel?psw=12345678"
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



app = dash.Dash()
app.layout = html.Div([
               html.H1("PROYECTO API SIATA"),
               dcc.Graph(figure=fig)
               ])

app.run_server(host='0.0.0.0',port=80)

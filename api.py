import flask
import pandas as pd

app = flask.Flask(__name__)

@app.route('/mostrar_estacionesnivel')
def mostrar_estacionesnivel():
  data = flask.request.args
  url = "http://siata.gov.co:8089/estacionesNivel/cf7bb09b4d7d859a2840e22c3f3a9a8039917cc3/?format=json"
  captura_web = pd.read_json(url,convert_dates='True')
  if data['psw'] == '12345678':
    print(captura_web)
    return captura_web.to_dict()
    return "Access"
  else:
    return "permiso no autorizado"

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5000)

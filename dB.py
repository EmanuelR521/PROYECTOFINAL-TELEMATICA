from flask import Flask
app = Flask(__name__)

@app.route("/recibir_DB")

def devuelveDB():

  data = {'user': ['carlos', 'ferney', 'emanuel'],
        'password': ["123", "123", "123"]}

  return data


if __name__ == '__main__':
   app.run(host='0.0.0.0',port=1002)

from flask import Flask
import pandas as pd
app = Flask(__name__)

@app.route("/dB")

def returnDB():

  data = {'user': ['carlos', 'ferney', 'emanuel'],
        'password': ["123", "123", "123"]}

  return data


if __name__ == '__main__':
   app.run(host='0.0.0.0',port=1002)


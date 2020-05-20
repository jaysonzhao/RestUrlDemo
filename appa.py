#!/usr/bin/env python3

import connexion
import socket
import requests
import os
from connexion import NoContent

# 发送请求
def post_mean(array: list):
    try:
        myurl = os.environ["MYURL"]
        r = requests.get(myurl)
        getresult = r.text
        return '{result}'.format(result=getresult)
    except Exception as inst:
        print(inst)
        return NoContent, 404



if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=8080, specification_dir='swagger/')
    hostname = socket.gethostname()
    app.add_api('demohub-api.yaml', arguments={'title': 'Solar Calculation Hub', 'host': hostname+':8080'})
    app.run()

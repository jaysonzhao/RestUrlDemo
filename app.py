#!/usr/bin/env python3

import connexion
import numpy as np
import socket
from connexion import NoContent

# 计算平均值
def post_mean(array: list):
    try:
        # 求均值
        calresult = np.mean(array)
        return '{result}'.format(result=calresult)
    except:
        return NoContent, 404


# 计算标准差
def post_std(array: list):
    try:
        # 求标准差
        calresult = np.std(array)
        return '{result}'.format(result=calresult)
    except:
        return NoContent, 404



if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=8080, specification_dir='swagger/')
    hostname = socket.gethostname()
    app.add_api('demohub-api.yaml', arguments={'title': 'Solar Calculation Hub', 'host': hostname+':8080'})
    app.run()

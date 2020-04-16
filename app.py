#!/usr/bin/env python3

import connexion
import numpy as np
import pandas as pd
import socket
from connexion import NoContent
from arch import arch_model  # GARCH(1,1)
from scipy import stats
from dfa import dfa
import scipy.signal as signal

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
    app.add_api('solarcalhub-api.yaml', arguments={'title': 'Solar Calculation Hub', 'host': hostname+':8080'})
    app.run()

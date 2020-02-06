# -*- coding: utf-8 -*-
"""

"""
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

import os


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    env_port = int(os.environ.get("PORT", 5000))
    env_debug = os.environ.get("FLASK_DEBUG", 1)
    # Dockerfile o run tenemos la opcion de la varaible de entorno FLASK_DEBUG = 1/0
    # docker build .... --build-arg FLASK_ENV="development"
    # docker run ........ -e "FLASK_ENV=production"
    app.run(host="0.0.0.0", port=env_port, debug=env_debug)

# copiar archivos o carpetas y sacar archivos, carpetas dentro del ordenador en local
# pasa archivos desde el contenedor auqneu este parado
# docker cp idcontentdor:/app carpetalocal
# se puede usar para testeo
# generar un docker desde el punto 0 .... y generar otro proyecto






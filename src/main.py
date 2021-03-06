# -*- coding: utf-8 -*-
"""

"""
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

import os

# instanciaiones
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

# git rm quitar elementos en el repositodio local
# git add añadir elementos en el repositorio local

# git diff --cehced
# git diff head

#  git config user.name
# git config --global user.name
# git config --global user.email
# cat .git/config

# tirar para atras
# git reset HEAD..

# tirar para atras
# git reset head --nombredel archivo

# git clone usuario@servidor:proyecto.git
# que es mejor github o gitlab.
# github ==> todo el mundo lo utiilzaba pero se han salido
# gitlab ==> el mas joven CI/CD(mas manager de proyecto)
# git remote -v
# git remote add origin 


# git branch cmabiar rama
# git push readme.md

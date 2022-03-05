#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0
# Copyright (c) 2022
# Amy Iris Parker <apark0006@student.cerritos.edu>
#
# This code is licensed under the Affero GNU Public License
# at version 3. For more, see <https://gnu.org/licenses>.

import os
from flask import Flask
import random
import string


def gen_random(count: int) -> str:
    base = list(string.ascii_letters) \
         + list(string.digits) \
         + list(string.punctuation)
    return ''.join(random.choice(base) for i in range(count))


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = gen_random(1024),
        DATABASE = os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # instance config if exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        # probably already exists
        pass

    @app.route('/hello')
    def hello():
        return "Hello, World!"

    return app

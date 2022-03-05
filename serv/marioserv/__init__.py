#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0
# Copyright (c) 2022
# Amy Iris Parker <apark0006@student.cerritos.edu>
#
# This code is licensed under the Affero GNU Public License
# at version 3. For more, see <https://gnu.org/licenses>.

import os
from flask import Flask, jsonify, request
import random
import string
import mysql.connector
import time

ghost = "localhost"
guser = "mario"
gpass = "secureddatabase"
gdb = "mario"


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

    app.config.update(
        mhost=ghost,
        muser=guser,
        mpassword=gpass,
        mdb=gdb
    )

    app.config["mysql"] = mysql.connector.connect(
        host=app.config["mhost"],
        user=app.config["muser"],
        password=app.config["mpassword"],
        database=app.config["mdb"]
    )

    @app.route("/hello", methods=["GET"])
    def hello():
        return "Hello, World!"

    @app.route("/listg", methods=["GET"])
    def listg():
        cur = app.config["mysql"].cursor()
        sql = "SELECT id FROM game"
        cur.execute(sql)
        res = [n[0] for n in cur.fetchall()]
        cur.close()
        return jsonify(res)

    @app.route("/new", methods=["GET"])
    def new():
        nid = ''.join(random.choice(
            list(string.ascii_letters + string.digits)
        ) for n in range(4))
        cur = app.config["mysql"].cursor()
        sql = "SELECT id FROM game"
        cur.execute(sql)
        vals = [str(n[0]) for n in cur.fetchall()]
        if nid in vals or nid == "0000":
            return jsonify(["0000"])
        sql = "INSERT INTO game(id, pc, sts) VALUES (%s, 0, %s)"
        dat = (nid, time.time_ns()//1000)
        cur.execute(sql, dat)
        app.config["mysql"].commit()
        cur.close()
        return jsonify([nid])

    @app.route("/update", methods=["POST"])
    def update():
        query = {
            "gid": str(request.form["gid"]),
            "pid": int(request.form["pid"]),
            "coins": int(request.form["coins"]),
            "xpos": int(request.form["xpos"]),
            "ypos": int(request.form["ypos"]),
            "lives": int(request.form["lives"]),
            "fin": bool(request.form["fin"])
        }
        sql = "UPDATE player SET coins = %s, xpos = %s, ypos = %s, "\
            "lives = %s, fin = %s WHERE pid = %s AND gid = %s"
        dat = [
            query["coins"],
            query["xpos"],
            query["ypos"],
            query["lives"],
            query["fin"],
            query["pid"],
            query["gid"]
        ]
        cur = app.config["mysql"].cursor()
        cur.execute(sql, dat)
        app.config["mysql"].commit()



    @app.route("/newp", methods=["GET"])
    def newp():
        gid = request.args["gid"]
        sql = "SELECT pc FROM game WHERE id = %s"
        dat = [gid]
        cur = app.config["mysql"].cursor()
        cur.execute(sql, dat)
        pc = cur.fetchall()[0][0]
        sql = "INSERT INTO player(pid, gid, coins, xpos, ypos, lives, fin, tf)"\
            " VALUES (%s, %s, %s, %s, %s, %s, %s, null)"
        dat = [pc, gid, 0, 0, 0, 3, 0]
        cur.execute(sql, dat)
        sql = "UPDATE game SET pc = %s WHERE id = %s"
        dat = [pc+1, gid]
        cur.execute(sql, dat)
        app.config["mysql"].commit()
        cur.close()
        return jsonify([pc])

    return app

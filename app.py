# python.exe -m venv .venv
# cd .venv/Scripts
# activate.bat
# py -m ensurepip --upgrade
# pip install -r requirements.txt

from flask import Flask

from flask import render_template
from flask import request
from flask import jsonify, make_response

import mysql.connector

import datetime
import pytz

from flask_cors import CORS, cross_origin

con = mysql.connector.connect(
    host="82.197.82.90",
    database="u861594054_prac8_awi",
    user="u861594054_fany_sl06",
    password="h>0ODuE^8X"
)

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    if not con.is_connected():
        con.reconnect()

    con.close()

    return render_template("index.html")

@app.route("/app")
def app2():
    if not con.is_connected():
        con.reconnect()

    con.close()

    return "<h5>Hola, soy Fany B)</h5>"
    
# Asistencias
@app.route("/asistencias")
def asistencias():
    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor(dictionary=True)
    sql    = """
    SELECT idAsistencia,
           idEmpleado,
           idReporte,
           estado

    FROM asistencias

    LIMIT 10 OFFSET 0
    """

    cursor.execute(sql)
    registros = cursor.fetchall()

    # Si manejas fechas y horas
    """
    for registro in registros:
        fecha_hora = registro["Fecha_Hora"]

        registro["Fecha_Hora"] = fecha_hora.strftime("%Y-%m-%d %H:%M:%S")
        registro["Fecha"]      = fecha_hora.strftime("%d/%m/%Y")
        registro["Hora"]       = fecha_hora.strftime("%H:%M:%S")
    """

    return render_template("asistencias.html", asistencias=registros)

# Empleados
@app.route("/empleados")
def empleados():
    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor(dictionary=True)
    sql    = """
    SELECT idEmpleado,
           nombreEmpleado,
           numero,
           fechaIngreso

    FROM empleados

    LIMIT 10 OFFSET 0
    """

    cursor.execute(sql)
    registros = cursor.fetchall()

    # Si manejas fechas y horas
    """
    for registro in registros:
        fecha_hora = registro["Fecha_Hora"]

        registro["Fecha_Hora"] = fecha_hora.strftime("%Y-%m-%d %H:%M:%S")
        registro["Fecha"]      = fecha_hora.strftime("%d/%m/%Y")
        registro["Hora"]       = fecha_hora.strftime("%H:%M:%S")
    """

    return render_template("empleados.html", empleados=registros)


#Reportes
@app.route("/reportes")
def reportes():
    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor(dictionary=True)
    sql    = """
    SELECT idReporte,
           fecha,
           comentarios

    FROM reportes

    LIMIT 10 OFFSET 0
    """

    cursor.execute(sql)
    registros = cursor.fetchall()

    # Si manejas fechas y horas
    """
    for registro in registros:
        fecha_hora = registro["Fecha_Hora"]

        registro["Fecha_Hora"] = fecha_hora.strftime("%Y-%m-%d %H:%M:%S")
        registro["Fecha"]      = fecha_hora.strftime("%d/%m/%Y")
        registro["Hora"]       = fecha_hora.strftime("%H:%M:%S")
    """

    return render_template("reportes.html", reportes=registros)

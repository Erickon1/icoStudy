#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf8
from flask import Flask, render_template,request, session, redirect, url_for,flash, jsonify
from config import DevelopmentConfig
from models import *
import forms

app = Flask(__name__)
app.config.from_object('config')
app.config.from_object(DevelopmentConfig)

   
@app.errorhandler(404)
def not_found(error):
	return "Not Found."

@app.errorhandler(500)
def server_error(e):
    return 'An internal error occurred.', 500


@app.before_request
def before_request():
    '''
    if 'username' not in session and request.endpoint in ['home','apunte','busqueda','mat','sem','titulo']:
       return redirect(url_for('login'))
    '''


@app.route(r'/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route(r'/login', methods=['GET','POST'])
def login():
    form_log = forms.LoginForm(request.form)
    form_reg = forms.RegisterForm(request.form)
    e = ""
    h=''
    i=''
    b=''
    c=''
    if request.method== 'POST' and form_log.validate():
        user= form_log.username.data
        password= form_log.password.data

        a = LoginModel(str(user))
        if a[2]:
            if a[0] == str(user) and a[1] == str(password):
                session['username'] = user
                return redirect(url_for('home'))
            else:
                e = "usuario o contraseña incorrectos"
        else:
            e = "usuario o contraseña incorrectos"

    return render_template('login.html', form=form_log , fo=form_reg, e=e)



@app.route(r'/register', methods=['GET','POST'])
def register():
    form_log = forms.LoginForm(request.form)
    form_reg = forms.RegisterForm(request.form)
    err=''
    h=''
    i=''
    d=''
    if request.method== 'POST' and form_reg.validate():
        user= (form_reg.username.data).encode('utf-8')
        email= form_reg.email.data
        password= (form_reg.password.data).encode('utf-8')

        a = ScanUser(unicode(str(user), "utf-8"))
        for x in a:
            h= x.username
            i= x.email
        b= str(h)
        c= str(i)
        a = ScanEmail(str(email))
        for x in a:
            i= x.email
        d= str(i)
        if b == user or c == email or d == email:
            err = 'usuario ya registrado'
        else:
            if SaveUser(unicode(str(user), "utf-8"),unicode(str(password), "utf-8"),str(email)):
                session['username'] = unicode(user,"utf-8")
                return redirect(url_for('home'))
    return render_template('login.html', form=form_log , fo=form_reg, e=err)

@app.route(r'/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route(r'/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('index'))


@app.route(r'/apunte', methods=['GET','POST'])
def apunte():
    form_save = forms.SaveData(request.form)
    e=""
    if request.method== 'POST' and form_save.validate():
        semestre= (form_save.semestre.data).encode('utf-8')
        titulo = (form_save.titulo.data).encode('utf-8')
        materia=(form_save.materia.data).encode('utf-8')
        profesor=(form_save.profesor.data).encode('utf-8')
        code=(form_save.code.data).encode('utf-8')
        x=datosCorrectos(int(semestre),str(materia))
        if (x[0]==True):
            if SaveText(session['username'],unicode(str(titulo), "utf-8"),int(semestre),str(materia),unicode(str(profesor), "utf-8"),unicode(str(code), "utf-8")):
                return ' <h3>bien hecho, quieres crear un apunte nuevo? <a href="/apunte"> si </a> o <a href="/home"> no </a> </h3>'
            else:
                return '<h3>error fatality vuelve a <a href="/apunte"> intentar </a></h3>'
        else:
            e=x[1]
            return render_template('formSaveData.html', fo=form_save, e=e )
    return render_template('formSaveData.html', fo=form_save, e=e )


def datosCorrectos(sem,mat):
    v=sem
    t=mat
    bool=True
    e=""
    if (v==1 ):
        if (t=="Algebra" or
            t=="Computadoras y Programacion" or
            t=="Calculo Diferencial e Integral" or
            t=="Introduccion a la ingenieria en computacion" or
            t=="Geometria analitica" ):
            print "Bien"
        else:
            e="Semestre y materia no coinciden Vuelve a intentar."
            bool=False

    elif(v==2):
        if (t=="Programacion Orientada a objetos" or
        t=="Algebra Lineal" or
        t=="Comunicacion Oral y Escrita" or
        t=="Calculo Vectorial" or
        t=="Administracion Contabilidad y Costos" ):
            print "Bien"
        else:
            e="Semestre y materia no coinciden Vuelve a intentar."
            bool=False

    elif(v==3):
        if (t=="Electricidad y Magnetismo" or
        t=="Metodos Numericos" or
        t=="Ecuaciones Diferenciales" or
        t=="Estructura de Datos" or
        t=="Introduccion a la Economia"):
            print "Bien"
        else:
            e="Semestre y materia no coinciden Vuelve a intentar."
            bool=False
    elif(v==4):
        if (t=="Investigacion de Operaciones y Sistemas" or
        t=="Analisis de Circuitos Electricos" or
        t=="Estructuras Discretas" or
        t=="Ingenieria Economica" or
        t=="Probabilidad y Estadistica" ):
            print "Bien"
        else:
            e="Semestre y materia no coinciden Vuelve a intentar."
            bool=False
    elif(v==5):
        if (t=="Diseno y Analisis de Algoritmos" or
        t=="Dispositivos Electronicos" or
        t=="Lenguajes Formales y Automatas" or
        t=="Medicion e Instrumentacion" or
        t=="Programacion de Sistemas"):
            print "Bien"
        else:
            e="Semestre y materia no coinciden Vuelve a intentar."
            bool=False
    elif(v==6):
        if (t=="Calidad" or
        t=="Compiladores" or
        t=="Diseno Logico" or
        t=="Ingenieria de software 1" or
        t=="Sistemas de Comunicaciones" or
        t=="Sistemas Operativos"):
            print "Bien"
        else:
            e="Semestre y materia no coinciden Vuelve a intentar."
            bool=False

    elif(v==7):
        if (t=="Bases de Datos 1" or
        t=="Dinamica de Sistemas Fisicos" or
        t=="Diseno de Sistemas Digitales" or
        t=="Redes de Computadoras 1" or
        t=="Seguridad Informatica"):
            print "Bien"
        else:
            e="Semestre y materia no coinciden Vuelve a intentar."
            bool=False

    elif(v==8):
        if (t=="Microprocesadores y Microcontroladores" or
        t=="Organizacion y Administracion de Centros de Computo" or
        t=="Sistemas de Control" or
        t=="Sistemas de Informacion"):
            print "Bien"
        else:
            e="Semestre y materia no coinciden Vuelve a intentar."
            bool=False
    elif(v==9):
        if (t=="Gestion de Redes de Computadoras" or
        t=="Habilidades Directivas" or
        t=="Inteligencia Artificial"):
            print "Bien"
        else:
            e="Semestre y materia no coinciden Vuelve a intentar."
            bool=False
    else:
        bool=False
    return [bool,e]

@app.route(r'/busqueda', methods=['GET','POST'])
def busqueda():
    form_save = forms.SaveData(request.form)

    return render_template('formScanText.html', fo=form_save )

@app.route(r'/sem', methods=['GET','POST'])
def sem():
    form_save = forms.SaveData(request.form)
    if request.method== 'POST':
        semestre= form_save.semestre.data
        a=ScanTextSemestre(int(semestre))
        return render_template('apuntes.html',a=a)
    return render_template('formScanText.html', fo=form_save )

@app.route(r'/mat', methods=['GET','POST'])
def mat():
    form_save = forms.SaveData(request.form)
    if request.method== 'POST':
        semestre= form_save.materia.data
        a=ScanTextMateria(semestre)
        return render_template('apuntes.html',a=a)
    return render_template('formScanText.html', fo=form_save )

@app.route(r'/titulo', methods=['GET','POST'])
def titulo():
    form_save = forms.SaveData(request.form)
    if request.method== 'POST':
        semestre= form_save.titulo.data
        a=ScanTextTitulo(semestre)
        return render_template('apuntes.html',a=a)
    return render_template('formScanText.html', fo=form_save )

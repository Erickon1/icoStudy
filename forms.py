#!/usr/bin/env python
# coding=utf-8
# coding: utf8
from wtforms import Form, StringField, PasswordField, validators, TextAreaField, SelectField
from wtforms.fields.html5 import EmailField


class LoginForm(Form):
    username= StringField('Username',
                          [
                              validators.Required(message='Obligatorio'),
                              validators.length(min=4, max=25, message='Nombre invalido,'
                                                                       'minimo 4 caracteres, maximo 25')
                          ])

    password= PasswordField('Password',
                            [
                                validators.Required(message='Obligatorio'),
                                validators.length(min=4, max=25, message='Password invalido,'
                                                                         'minimo 4 caracteres, maximo 25')
                            ])


class RegisterForm(Form):
    username= StringField('Username',
                          [
                              validators.Required(message='Obligatorio'),
                              validators.length(min=4, max=25, message='Nombre invalido,'
                                                                       'minimo 4 caracteres, maximo 25')
                          ])

    password= PasswordField('Password',
                            [
                                validators.Required(message='Obligatorio'),
                                validators.length(min=4, max=25, message='Password invalido,'
                                                                         'minimo 4 caracteres, maximo 25')
                            ])

    email= EmailField('Email',
                      [
                          validators.Required(message='Obligatorio'),
                          validators.Email(message='E-mail invalido')
                      ])

class SaveData(Form):
    titulo= StringField('Titulo',
                          [
                              validators.Required(message='Obligatorio'),
                              validators.length(min=4, max=25, message='Titulo invalido,'
                                                                       'minimo 4 caracteres, maximo 25')
                          ])
    semestre = SelectField('Semestre', choices=[('1', '1'), ('2', '2'),('3', '3'),
                                                ('4', '4'), ('5', '5'), ('6', '6'),
                                                ('7', '7'), ('8', '8'), ('9','9')])
    materia = SelectField('Materia', choices=[
        ('Algebra', '1-Algebra'), ('Computadoras y Programacion', '1-Computadoras y Programacion'),
        ('Calculo Diferencial e Integral', '1-Calculo Diferencial e Integral'),
        ('Introduccion a la ingenieria en computacion', '1-Introduccion a la ingenieria en computacion'),
        ('Geometria analitica', '1-Geometria analitica'),

        ('Programacion Orientada a objetos', '2-Programacion Orientada a objetos'), ('Algebra Lineal', '2-Algebra Lineal'),
        ('Comunicacion Oral y Escrita', '2-Comunicacion Oral y Escrita'),
        ('Calculo Vectorial', '2-Calculo Vectorial'), ('Administracion Contabilidad y Costos', '2-Administracion Contabilidad y Costos'),

        ('Electricidad y Magnetismo', '3-Electricidad y Magnetismo'), ('Metodos Numericos', '3-Metodos Numericos'),
        ('Ecuaciones Diferenciales', '3-Ecuaciones Diferenciales'),
        ('Estructura de Datos', '3-Estructura de Datos'), ('Introduccion a la Economia', '3-Introduccion a la Economia'),

        ('Investigacion de Operaciones y Sistemas','4-Investigacion de Operaciones y Sistemas'),
        ('Analisis de Circuitos Electricos', '4-Analisis de Circuitos Electricos'),
        ('Estructuras Discretas', '4-Estructuras Discretas'),
        ('Ingenieria Economica', '4-Ingenieria Economica'), ('Probabilidad y Estadistica', '4-Probabilidad y Estadistica'),

        ('Diseno y Analisis de Algoritmos', '5-Diseno y Analisis de Algoritmos'), ('Dispositivos Electronicos', '5-Dispositivos Electronicos'),
        ('Lenguajes Formales y Automatas', '5-Lenguajes Formales y Automatas'),
        ('Medicion e Instrumentacion', '5-Medicion e Instrumentacion'), ('Programacion de Sistemas', '5-Programacion de Sistemas'),

        ('Calidad', '6-Calidad'), ('Compiladores', '6-Compiladores'), ('Diseno Logico', '6-Diseno Logico'),
        ('Ingenieria de software 1', '6-Ingenieria de software 1'),
        ('Sistemas de Comunicaciones', '6-Sistemas de Comunicaciones'), ('Sistemas Operativos', '6-Sistemas Operativos'),

        ('Bases de Datos 1', '7-Bases de Datos 1'), ('Dinamica de Sistemas Fisicos', '7-Dinamica de Sistemas Fisicos'),
        ('Diseno de Sistemas Digitales', '7-Diseno de Sistemas Digitales'),
        ('Redes de Computadoras 1', '7-Redes de Computadoras 1'), ('Seguridad Informatica', '7-Seguridad Informatica'),

        ('Microprocesadores y Microcontroladores', '8-Microprocesadores y Microcontroladores'),
        ('Organizacion y Administracion de Centros de Computo', '8-Organizacion y Administracion de Centros de Computo'),
        ('Sistemas de Control', '8-Sistemas de Control'), ('Sistemas de Informacion', '8-Sistemas de Informacion'),

        ('Gestion de Redes de Computadoras', '9-Gestion de Redes de Computadoras'), ('Habilidades Directivas', '9-Habilidades Directivas'),
        ('Inteligencia Artificial', '9-Inteligencia Artificial')

    ])
    profesor= StringField('Profesor',
                            [
                                validators.Required(message='Obligatorio'),
                                validators.length(min=4, max=25, message='Profesor incorrecto, '
                                                                         'minimo 4 caracteres, maximo 25')
                            ])
    code = TextAreaField('Ingresa tu texto',
                         [
                             validators.Required(message='Obligatorio'),
                         ])


class LoadData(Form):
    username= StringField('Username',
                          [
                              validators.Required(message='Obligatorio'),
                              validators.length(min=4, max=25, message='Nombre invalido,'
                                                                       'minimo 4 caracteres, maximo 25')
                          ])

    password= PasswordField('Password',
                            [
                                validators.Required(message='Obligatorio'),
                                validators.length(min=4, max=25, message='Password invalido,'
                                                                         'minimo 4 caracteres, maximo 25')
                            ])

    email= EmailField('Email',
                      [
                          validators.Required(message='Obligatorio'),
                          validators.Email(message='E-mail invalido')
                      ])

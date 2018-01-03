#!/usr/bin/env python
# coding=utf-8
# coding: utf8
from google.appengine.ext import ndb
from google.appengine.datastore.datastore_query import *

class User(ndb.Model):
    username = ndb.StringProperty(indexed=True, required=True)
    password = ndb.StringProperty(indexed=True, required=True)
    email = ndb.StringProperty(indexed=True, required=True)

class Text(ndb.Model):
    user = ndb.StringProperty(indexed= True, required=True)
    titulo = ndb.StringProperty(indexed= True, required=True)
    semestre = ndb.IntegerProperty(indexed= True, required=True)
    materia = ndb.StringProperty(indexed= True, required=True)
    profesor = ndb.StringProperty(indexed= True, required=True)
    code = ndb.TextProperty(indexed= True, required=True)

def SaveUser(usernam,passwor,email):
    try:
        a=User(
            email=email,
            password=passwor,
            username=usernam
        )
        a.put()
        return True
    except:
        return False


def ScanUser(name):
    try:
        xxx= User.query(User.username == name).fetch()
    except:
        xxx='error'
    return xxx

def ScanEmail(name):
    xxx= User.query(User.email == name).fetch()#verificar la consulta por nombre
    return xxx


def ScanData(dato):
    """
    #q= ndb.Query("SELECT * FROM User")
    #q= User._get_kind() #esta si sirve
    #q= ndb.Key(User,'username')
    o = ndb.QueryOptions(keys_only=True, offset=20)
    #results = qry.fetch(10, options=qo)
    #results = qry.fetch(10, keys_only=True, offset=20)
    sa = ndb.Key(User, 'mausontlas@gmail.com')
    n = ndb.Model.allocate_ids(size=1, parent=sa)[0]
    q=ndb.gql("SELECT * FROM User WHERE username = 'Oscar' ")
    r=User.query(User.username == 'Oscar').fetch(10,offset=20)
    p= ndb.Model._lookup_model('User')
    """
    qry = User.query(User.username != " " ).filter().order() # Create a query
    for acct in qry.fetch(10, offset=20): # Skip the first 20
        print acct
    alpha=str(qry.fetch(10, offset=20))
    xxx=qry.fetch(5, offset=20)
    print xxx
    return xxx

    """
    User.get(User.username == username, check_password_hash(User.get(User.username == username)._data['password'],password))
    ndb.get_multi()
    q= ndb.Query("SELECT * FROM User ")
    """

def SaveText(user = 'Anonimo',titulo = 'Primer Apunte',semestre = 1,materia = 'Programacion',profesor = 'GDG',code = 'Este es el apunte que deberia de escribir el usuario'):
    try:
        guido = Text(
            user=user,
            titulo = titulo,
            semestre=semestre,
            materia = materia,
            profesor = profesor,
            code = code
        )
        guido.put()
        return True
    except:
        return False

def LoginModel(user):
    try:
        a = ScanUser(str(user))
        for x in a:
            h= x.username
            i= x.password
        b= str(h)
        c= str(i)
        return [b,c,True]
    except:
        return False


def ScanTextMateria(dato):
    xxx=Text.query(Text.materia == dato).fetch()
    return xxx

def ScanTextSemestre(dato):
    xxx=Text.query(Text.semestre == dato).fetch()
    return xxx

def ScanTextTitulo(dato):
    xxx=Text.query(Text.titulo == dato).fetch()
    return xxx
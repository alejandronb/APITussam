#coding: utf-8
from suds.client import Client
import webbrowser
from lxml import etree


linea = raw_input("Introduzca el número de línea que desea consultar: ")

cliente = Client('http://www.infobustussam.com:9001/services/dinamica.asmx?wsdl', retxml=True)

respuesta = cliente.service.GetStatusLinea("%s" % linea)
raiz = etree.fromstring(respuesta.encode("utf-8"))
raiz2 = raiz[0][0]

ns = "{http://tempuri.org/}"

#print etree.tostring(raiz2, pretty_print=True)

result = raiz2.find(ns+"GetStatusLineaResult")
activos = result.find(ns+"activos")
frec = result.find(ns+"frec_bien")
graves = result.find(ns+"graves")
act = activos.text
frec1 = frec.text
grav = graves.text

print "Numero de vehiculos activos: %s" % act
print "De los cuales van bien de frecuencia: %s" % frec1
print "Numero de vehiculos que han sufrido accidentes graves: %s" % grav


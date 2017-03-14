#!/usr/bin/python3
#LAURA TRABAS CLAVERO

import webapp
import random

class aleatApp(webapp.app):

    def process(self,parsedRequest):
        URL = str(random.randint(0,100000000))
        numero = "/aleat/" + URL
        return ("200 OK", "<html><body><a href= '"+ numero +"'>Hola, Dame otra</a></body></html>")

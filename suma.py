#!/usr/bin/python3
#LAURA TRABAS CLAVERO

import webapp

class sumaApp(webapp.app):
    def parse(self, request,rest):
        return rest.split('/')[1:]
    def process(self, parsedRequest):
        """Process the relevant elements of the request.
        Returns the HTTP code for the reply, and an HTML page.
        """
        num1 = int(parsedRequest[0])
        num2 = int(parsedRequest[1])
        resultado = num1 + num2
        return ("200 OK","<html><body<h1>La suma es: " + str(num1) +
                "+" + str(num2) + "=" + str(resultado)+ "</h1></body></html>")

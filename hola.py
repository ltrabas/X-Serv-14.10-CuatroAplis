#!/usr/bin/python3
#LAURA TRABAS CLAVERO

import webapp

class holaApp(webapp.app):

    def process(self, parsedRequest):
        """Process the relevant elements of the request.
        Returns the HTTP code for the reply, and an HTML page.
        """

        return ("200 OK", "<html><body><h1>" + "¡Hola!" + "</h1></body></html>")

class adiosApp(webapp.app):
    def process(self, parsedRequest):
        """Process the relevant elements of the request.
        Returns the HTTP code for the reply, and an HTML page.
        """

        return ("200 OK", "<html><body><h1>" + "¡Adios!" + "</h1></body></html>")

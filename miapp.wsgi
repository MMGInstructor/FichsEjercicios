import os, sys
 
sys.path.append('/ruta/a/application')
 
def application(environ, start_response):
    output = "&amp;lt;b&amp;gt;Hola Mundo!&amp;lt;/b&amp;gt;"
    start_response('200 OK', 
                   [('Content-Type', 
                     'text/html; charset=utf-8')])
 
    return output
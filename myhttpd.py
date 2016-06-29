# -*-coding:utf-8 -*-
# File Name: myhttpd.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python

from os import curdir,sep

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            f = open(curdir + sep + self.path)
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()

        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)


def main():
    try:
        server = HTTPServer(('192.168.1.1',7779),MyHandler)
        print 'Welcome to the machine...'
        print 'Press ^C onec or twice to quit.'
        server.serve_forever()

    except KeyboardInterrupt:
        print '^C received,shutting down server'
        server.socket.close()


if __name__ == '__main__':
    main()

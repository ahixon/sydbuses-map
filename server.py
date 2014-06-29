#!/usr/bin/python
import urllib2
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import pprint 
import json

PORT_NUMBER = 8080

class myHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path.startswith ('/vehicles'):
			opener = urllib2.build_opener()

			# Pretend to be an old version of iPhone TripView Lite.
			opener.addheaders = [('User-agent', 'TripViewLite/212 CFNetwork/609 Darwin/13.0.0')]
			routestr = ','.join(ROUTES)
			response = opener.open('http://realtime.grofsoft.com/tripview/vehicles?routes=%s' % routestr)

			data = response.read()
			pprint.pprint(json.loads(data))	# pretty print for debugging
			response.close()

			self.send_response(200)
			self.send_header('Content-type', 'application/json')
			self.end_headers()

			# Send same JSON back to client
			self.wfile.write(data)
		else:
			html = open ('busmap.html').read()
			self.wfile.write (html)

		return

try:
	ROUTES = [line.strip() for line in open('routes.txt')]
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started server at http://localhost:%d/' % PORT_NUMBER
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()

from __future__ import print_function
from gevent.server import DatagramServer
from ait.core import log

class tlmChannel(DatagramServer):

	def handle(self, data, address): 
		print(data)

if __name__ == '__main__':
	log.info('Starting Telemetry Channel Server')
	tlmChannel(':9000').serve_forever()




from __future__ import print_function
from gevent.server import DatagramServer
from ait.core import log

class UDPServer(object):

    def __init__(self, host):
        self.udp_server = DatagramServer(host, handle=self.handler)
        self.udp_server.start()

    def __repr__(self):
        return "<UDPServer id={} started: {}>".format(id(self),
                                                      self.udp_server.started)

    def handler(self, data, address):
        print "{}: got data {} from {}".format(self, data, address)

    def stop(self):
        self.udp_server.close()
	
if __name__ == '__main__':
	log.info('Starting Telemetry Channel Server')
	tlmChannel(':9000').serve_forever()




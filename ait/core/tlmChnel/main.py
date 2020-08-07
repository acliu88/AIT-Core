import argparse
from ait.core import log
from tlmServer import tlmChannel
from gevent.server import DatagramServer

'''
Usage: ait-channelTlm

Starts up server to read in telemetry and 
build AIT Packets onces per second

	ap = argparse.ArgumentParser(
		description = __doc__,
		formatter_class = argparse.ArgumentDefaultsHelpFormatter
		)
	args = ap.parse_args()
'''

def main():
	
	log.info('Starting Telemetry Channel Server')
	tlmChannel(':3076').serve_forever()

if __name__ == '__main__':
	main()


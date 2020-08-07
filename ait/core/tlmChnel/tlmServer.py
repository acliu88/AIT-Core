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
        print ("{}: got data {} from {}".format(self, data, address))

    def stop(self):
        self.udp_server.close()
	
def sender(host, timeout=1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print ("start sending data to", host)
    with Timeout(timeout, exception=False):
        while(True):
            rand = random.random()
            print ("send", rand)
            sock.sendto(str(rand), host)
            sleep(.1)
    print ("sender finished")

def plain_datagram_server(host, port, time):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    print ("start plain UDP server for {}s".format(time))
    server_address = (host, port)
    print ('starting up on %s port %s' % server_address)
    sock.bind(server_address)
    print ("started plain datagram server")
    sleep(time)
    print ("stop plain datagram server")


def test_datagram_server(host):
    print ("DatagramServer test on", host)
    print ("Start udp1 on {} and send data".format(host))
    udp1 = UDPServer(host)
    sender_greenlet = spawn(sender, host)
    sender_greenlet.join()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["send", "test_plain"])
    parser.add_argument("--time", default=10)
    parser.add_argument("--port", default=8000)
    parser.add_argument("--host", default="localhost")

    args = parser.parse_args()
    if args.mode == "send":
        sender((args.host, args.port), args.time)
    elif args.mode == "test_plain":
        spawn(plain_datagram_server, args.host, args.port, args.time)
        sleep()
        test_datagram_server((args.host, args.port))





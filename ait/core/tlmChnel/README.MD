# Channelized Server Processor Documentation
#### General Information: Additional support for processing "channelized" telemetry fields into a single AIT packet.

Input port ----- Channelized telemetry ---->  "Channelized Server Processor ----> Complete AIT Packet at defined rate ---->  Output port

Background:
Various parts of AIT expect complete AIT packets when processing data. Certain situations, especially with different types of flight software, arise where data received is heavily channelized. In our context, a "channelized field" means that we're receiving a single telemetry field from a packet (or perhaps a few fields from a packet) at a given time instead of a single packet object.


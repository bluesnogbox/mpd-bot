#!/usr/bin/python

from mpd import MPDClient
client = MPDClient()               # create client object
client.timeout = 10                # network timeout in seconds (floats allowed), default: None
client.idletimeout = None          # timeout for fetching the result of the idle command is handled seperately, default: None
client.connect("bluesnogbox.duckdns.org", 6600)  # connect to URL:6600 (default port)

print(client.mpd_version)          # print the MPD version
print(client.listplaylists())

client.close()                     # send the close command
client.disconnect()                # disconnect from the server

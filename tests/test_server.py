
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import unittest
import time
import urllib
import urllib2
import json
import locaudio.db as db
import locaudio.api as api
import socket


server_addr = socket.gethostbyname(socket.getfqdn())
server_port = 8000

test_sound_name = "Cock"

loc = api.Locaudio(server_addr, server_port)

_, _, f_print = db.get_reference_data(test_sound_name)

d_dicts = [
    {
        "x": 56.3399723,
        "y": -2.8082881,
        "spl": 65,
        "timestamp": time.time() - 3,
        "fingerprint": f_print
    },
    {
        "x": 56.3399723,
        "y": -2.8082881,
        "spl": 65,
        "timestamp": time.time() - 1,
        "fingerprint": f_print
    },
    {
        "x": 56.3399723,
        "y": -2.8082881,
        "spl": 65,
        "timestamp": time.time() - 5,
        "fingerprint": f_print
    },
    {
        "x": 56.3399723,
        "y": -2.8082881,
        "spl": 65,
        "timestamp": time.time(),
        "fingerprint": f_print
    }
]


class ServerTest(unittest.TestCase):

    def test_server_notify(self):
        for d_dict in d_dicts:
            loc.notify_event(d_dict)

        print "\n=== Server Notify ===\n"


    def test_server_triangulation(self):
        pos_list = loc.get_sound_locations(test_sound_name)

        print "\n=== Server Triangulation === :: {0}\n".format(pos_list)


    def test_names(self):
        names_list = loc.get_names()

        print "\n=== Server Names === :: {0}\n".format(names_list)


if __name__ == "__main__":
    print "\n=== Server Testing ===\n"
    global server_addr
    if len(sys.argv) == 2:
        server_addr = sys.argv[1]
    unittest.main()


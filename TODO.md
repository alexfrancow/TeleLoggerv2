# Separar archivos, uno que cree un pyc (Corre en segundo plano) el cual tenga el keylogger en segundo plano recogiendo las teclas en un txt, 
y mientras el otro sirve de c&c con las funciones correspondientes para comunicarse con el mediante telegram; EJ: /send, envia el archivo txt 
donde se irán almacenando todas las pulsaciones.

EJ:

telelogger.py -- Contiene las funciones para dar ordenes mediante telegram, tambien es el que crea al otro py.

telelogger.pyc -- Es creado por el archivo principal, sirve para pillar todas las teclas e ir almacenandolas en un txt. (Debe correrse en
background y de manera discreta)


# Mirar forma de enviar pulsaciones en vivo.

# Intentar hacerlo sin dependencias (Telebot)




# Otra opcion, un archivo telelogger que genera un archivo, contiene un raw_imput que pregunta el TOKEN y chat_id, para luego
crear un archivo unico.

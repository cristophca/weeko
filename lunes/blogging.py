import logging

logging.warning('¡Cuidado!') # Por defecto a partir del nivel de warning el mensaje sale por pantalla

logging.info('Mira que te lo dije...') # este no aparecerá por que esta por debajo de warning

#si quiero cabiar el nivel por defecto
#logging.basicconfig(filename='Nombre fichero donde envia el mensaje',
# level=logging.DEBUG,
# format='%(asctime)s- %(message)s')#Muestra la marca temporal y el mensaje
#Si el fichero filename no existe lo crea y si existe graba el mensaje al final del fichero

#Para dar un nombre al logging de donde viene el mensaje
logger = logging.getLogger(__name__)
logger.info('es otro logger')

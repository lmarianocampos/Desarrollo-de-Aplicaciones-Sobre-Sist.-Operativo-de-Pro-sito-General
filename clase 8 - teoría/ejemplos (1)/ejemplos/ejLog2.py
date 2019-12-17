import logging
import logging.handlers
import time

#consultar con: tail /var/log/syslog | grep "MI_SERVICIO"

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address = '/dev/log')
formatter = logging.Formatter('MI_SERVICIO %(module)s.%(funcName)s: %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)

log.debug('Inicio de MiServicio. Mensaje de debug')
time.sleep(1)
log.info('Mensaje informativo')
time.sleep(1)

try:
	int("hola") #genero un error
except Exception as e:
	log.critical('Cierro servicio:'+str(e), exc_info=True)





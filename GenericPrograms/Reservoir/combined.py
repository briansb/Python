import logging

# add filemode="w" to overwrite
# will only write messages WARNING and above
logging.basicConfig(filename="sample.log", filemode="w", level=logging.WARNING)

logging.debug("This is a debug message")
logging.info("Informational message")
logging.warning("This is a warning message")
logging.error("An error has happened!")
logging.critical("This is critical.  Very bad")

logging.basicConfig(filename="sample.log", level=logging.INFO)
log = logging.getLogger("ex")

try:
    raise RuntimeError
except RuntimeError:
    log.exception("Error!")

import logging

logging.basicConfig(format="%(asctime)s / %(levelname)s : %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)

logging.warning("warning message")
logging.info("info message")
logging.critical("critical message")
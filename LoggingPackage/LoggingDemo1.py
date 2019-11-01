'''
Logging levels:
1. Critical
2. Error
3. Warning
4. Info
5. Debug
'''
import logging

'''
filename - log output file
level - treshold level of warnings
'''
logging.basicConfig(filename="test.log", level=logging.DEBUG)

logging.warning("warning message")
logging.info("info message")
logging.critical("critical message")
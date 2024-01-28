import logging
import sys

def run(name:str, streamLevel:str, logFile:str):
    level = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }[streamLevel.upper()]

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    fileHandler = logging.FileHandler(logFile)
    consoleHandler = logging.StreamHandler(sys.stdout)

    fileHandler.setLevel(logging.DEBUG)
    consoleHandler.setLevel(level)

    fileHandler.setFormatter(formatter)
    consoleHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    logger.addHandler(consoleHandler)

    def modifiedPrint(*args):
        s = ' '.join([str(a) for a in args])
        logger.info(s)

    return modifiedPrint


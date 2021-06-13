import inspect
import logging
import logging.config

class LogGen:
    @staticmethod
    def loggen(logLevel=logging.INFO):
        '''
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        #logging.basicConfig(filename=".\\Logs\\automation.log", format='%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger
'''
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        logger.setLevel(logging.INFO)

        fileHandler = logging.FileHandler(".\\Logs\\automation.log", mode='a')
        fileHandler.setLevel(logLevel)

        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        return logger
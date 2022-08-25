import inspect
import logging


class BaseClass:

    def log_method(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logFile.log')
        formatter_obj = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter_obj)
        logger.setLevel(logging.INFO)
        logger.addHandler(fileHandler)
        return logger


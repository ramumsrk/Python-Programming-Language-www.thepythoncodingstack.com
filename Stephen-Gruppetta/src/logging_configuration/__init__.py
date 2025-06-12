from logging import Logger
from logging import getLogger
from logging import DEBUG
from logging import StreamHandler
from logging import Formatter
from sys import stdout

# User-defined function
def logging_configuration() -> Logger:
    '''
    Configure a logging.Logger instance

    Return:
    -------
      Return a logging.Logger
      instance
    '''
    # Obtain a named logging.Logger
    # instance
    logger: Logger = getLogger(name = 'www.thepythoncodingstack.com')
    # Set logging level
    logger.setLevel(level = DEBUG)
    # Obtain a
    # logging.StreamHandler()
    # instance
    streamhandler: StreamHandler = StreamHandler(stream = stdout)
    # logging.LogRecord format
    fmt: str = f"%(asctime)s - %(name)s - %(levelname)s - %(process)d - %(processName)s - %(thread)d - %(threadName)s - %(pathname)s - %(filename)s - %(module)s - %(funcName)s - %(message)s"
    # DateTime format
    datetimefmt: str = F"%A, %B %d, %Y %H:%M:%S %Z"
    # Obtain a logging.Formatter()
    # instance
    formatter: Formatter = Formatter(fmt = fmt, datefmt = datetimefmt)
    # Set logging.StreamHandler
    # format to logging.Formatter
    streamhandler.setFormatter(formatter)
    # Add logging.StreamHandler to
    # logging.Logger instance
    logger.addHandler(streamhandler)
    return logger
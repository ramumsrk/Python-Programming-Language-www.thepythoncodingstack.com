#! /usr/bin/env -S python3.13 -v

from logging import Logger

from logging_configuration import logging_configuration
from are_python_dictionaries_ordered_data_structures.some_history_first import first_dictionary

# User-defined function
def main() -> None:
    '''
    An entry-point function

    Return:
    -------
      None
    '''
    logger: Logger = logging_configuration()
    logger.debug(F"{first_dictionary=}")
    for key, value in first_dictionary.items():
        logger.debug(F"Key is: '{key=}' and Value is: '{value=}'")
    return None

if __name__ == '__main__':
    # Function call
    main()
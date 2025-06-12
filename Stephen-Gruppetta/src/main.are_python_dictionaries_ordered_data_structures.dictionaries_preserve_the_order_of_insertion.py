#! /usr/bin/env -S python3.13 -v

from logging import Logger

from logging_configuration import logging_configuration
from are_python_dictionaries_ordered_data_structures.some_history_first import first_dictionary
from are_python_dictionaries_ordered_data_structures.dictionaries_preserve_the_order_of_insertion import second_dictionary, first_list, second_list

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
    logger.debug(F"{second_dictionary=}")
    logger.debug(F"{(first_dictionary == second_dictionary)=}")
    logger.debug(F"{first_list=}")
    logger.debug(F"{second_list=}")
    logger.debug(F"{(first_list == second_list)=}")
    return None

if __name__ == '__main__':
    # Function call
    main()
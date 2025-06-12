#! /usr/bin/env -S python3.13 -v

from logging import Logger

from are_python_dictionaries_ordered_data_structures.how_about_collections_OrderedDict import third_ordered_dictionary, fourth_ordered_dictionary
from logging_configuration import logging_configuration

# User-defined function
def main() -> None:
    '''
    An entry-point function

    Return:
    -------
      None
    '''
    logger: Logger = logging_configuration()
    logger.debug(F"{third_ordered_dictionary=}")
    logger.debug(F"{fourth_ordered_dictionary=}")
    logger.debug(F"{(third_ordered_dictionary == fourth_ordered_dictionary)=}")
    return None

if __name__ == '__main__':
    # Function call
    main()
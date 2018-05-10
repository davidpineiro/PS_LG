import sys
import argparse
import logging
from logging.config import fileConfig
from ConfigParser import ConfigParser
from utils import prime_generator
from utils import calculate_divisors

# Reading logging configuration
fileConfig('config/logging_config.ini')
logger = logging.getLogger()
logger.debug('Initializing logging configuration')

# Reading properties file
DEFAULT_PRIME_SEED = 100000
parser = ConfigParser()
parser.read('config/application.ini')
try:
    prime_seed = parser.get('environment', 'primes.seed')
    logger.info("Prime seed readed from configuration file, value is %s", prime_seed)
    prime_seed = int(prime_seed)
    if prime_seed < DEFAULT_PRIME_SEED:
        raise ValueError("Prime seed must be greater than %s)", DEFAULT_PRIME_SEED)
except:
    prime_seed = DEFAULT_PRIME_SEED
    logger.error("There is no valid prime seed value in config/application.ini configuration file or its value is less than the default one, default value applied will be %s", prime_seed)



def main(args):
    logger.debug('Running main file with parameter %s', args)
    calculate(args)



def calculate(number_list):
    """Calculates the type of number.
       If the sum of their divisors is exactly the number the it is perfect, else if the sum is lower than the number it is deficient
       and if the sum is greater than the number it is an abundant number.

    :param number_list: list with the numbers to calculate
    :returns: nothing, it will debug the number categorization
    """
    primes_list = prime_generator(prime_seed)
    for number in number_list:
        logger.debug("Calculating for %s", number)
        validnumber = toValidNumber(number)
        if validnumber < 0:
            continue
        divisors = calculate_divisors(validnumber, primes_list);
        logger.debug("Divisors are %s", divisors)
        total = sum(divisors)
        logger.debug("Sum is %s", total)
        if total == validnumber:
            logger.info ("Number %s is perfect", validnumber)
        elif total < validnumber:
            logger.info("Number %s is deficient", validnumber)
        else:
            logger.info("Number %s is abundant", validnumber)



def toValidNumber(candidate):
    try:
        val = int(candidate)
        if val < 2 or str(val) != str(candidate):  # if not a positive int print message and ask for input again
            logger.error("%s must be greater than 1 and it must be integer", candidate)
            return -1
    except ValueError:
        logger.error("%s is not a valid number", candidate)
        return -1
    return val



if __name__ == "__main__":
    logger.debug("Invoking main program with arguments %s", sys.argv )
    parser = argparse.ArgumentParser(description='Calculate divisors')
    parser.add_argument('numberlist', metavar='List', nargs='+',
                        help='list of natural numbers greater than 1, sepparated by blanks (for instance: 3 89 468)')

    args = parser.parse_args()
    main(args.numberlist)

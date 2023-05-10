import sys
import logging


def main():
    message = 'UNIQUE IDENTIFIER#1425'
    logging.debug(f'Debug: {message}')
    logging.info(f'Info: {message}')
    logging.warning(f'Warning: {message}')
    logging.error(f'Error: {message}')
    logging.critical(f'Critical: {message}')


if __name__ == "__main__":
    main()

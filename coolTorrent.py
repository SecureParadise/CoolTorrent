import logging
import sys
from torrent.cli import main

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error("An error occurred: %s", str(e))
        sys.exit(1)

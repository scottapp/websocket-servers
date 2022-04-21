from dotenv import load_dotenv
import logging
from ws_servers.alpaca import CrpytoServer


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    load_dotenv()

    server = CrpytoServer()
    server.run()

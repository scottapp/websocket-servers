from dotenv import load_dotenv
import pandas as pd
import numpy as np
import pymarketstore as pymkts
import logging

from ws_servers.alpaca import CrpytoServer


cli = pymkts.Client()


async def print_crypto_trade(t):
    print('crypto trade', t)


async def write_tick(data):
    global cli
    ticker = data['S']
    price = data['p']
    size = data['s']
    t = pd.to_datetime(data['t'].seconds, unit='s')
    data = np.array([(t.value / 10 ** 9, price, size)], dtype=[('Epoch', 'i8'), ('p', 'f4'), ('s', 'f4')])
    print(data)
    res = cli.write(data, '{}/1Min/Tick'.format(ticker))
    assert res['responses'] == None, res


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    load_dotenv()

    server = CrpytoServer()
    server.subscribe_crypto_trades(write_tick, 'BTCUSD')
    server.run()

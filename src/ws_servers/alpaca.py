import logging
from alpaca_trade_api.stream import Stream

log = logging.getLogger(__name__)


async def print_trade(t):
    print('trade', t)


async def print_quote(q):
    print('quote', q)


async def print_trade_update(tu):
    print('trade update', tu)


async def print_crypto_trade(t):
    print('crypto trade', t)


class CrpytoServer(object):
    def __init__(self):
        self.feed = 'iex'  # <- replace to SIP if you have PRO subscription
        self.stream = Stream(data_feed=self.feed, raw_data=True)
        # stream.subscribe_trade_updates(print_trade_update)
        self.stream.subscribe_trades(print_trade, 'AAPL')
        self.stream.subscribe_quotes(print_quote, 'IBM')
        self.stream.subscribe_crypto_trades(print_crypto_trade, 'BTCUSD')

        @self.stream.on_status("*")
        async def _(status):
            print('status', status)

        """
        @self.stream.on_bar('MSFT')
        async def _(bar):
            print('bar', bar)

        @self.stream.on_updated_bar('MSFT')
        async def _(bar):
            print('updated bar', bar)

        @self.stream.on_luld('AAPL', 'MSFT')
        async def _(luld):
            print('LULD', luld)
        """

    def run(self):
        self.stream.run()

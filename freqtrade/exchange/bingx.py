"""Bingx exchange subclass"""

import logging
from typing import Dict

from HuangTrader.exchange import Exchange


logger = logging.getLogger(__name__)


class Bingx(Exchange):
    """
    Bingx exchange class. Contains adjustments needed for HuangTrader to work
    with this exchange.
    """

    _ft_has: Dict = {
        "ohlcv_candle_limit": 1000,
        "stoploss_on_exchange": True,
        "stoploss_order_types": {"limit": "limit", "market": "market"},
        "order_time_in_force": ["GTC", "IOC", "PO"],
    }

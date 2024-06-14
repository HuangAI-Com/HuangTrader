from typing import Optional

from HuangTrader.exchange import Exchange
from HuangTrader.util.migrations.binance_mig import migrate_binance_futures_data
from HuangTrader.util.migrations.funding_rate_mig import migrate_funding_fee_timeframe


def migrate_data(config, exchange: Optional[Exchange] = None):
    migrate_binance_futures_data(config)

    migrate_funding_fee_timeframe(config, exchange)

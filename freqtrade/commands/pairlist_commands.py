import logging
from typing import Any, Dict

import rapidjson

from HuangTrader.configuration import setup_utils_configuration
from HuangTrader.enums import RunMode
from HuangTrader.resolvers import ExchangeResolver


logger = logging.getLogger(__name__)


def start_test_pairlist(args: Dict[str, Any]) -> None:
    """
    Test Pairlist configuration
    """
    from HuangTrader.persistence import FtNoDBContext
    from HuangTrader.plugins.pairlistmanager import PairListManager

    config = setup_utils_configuration(args, RunMode.UTIL_EXCHANGE)

    exchange = ExchangeResolver.load_exchange(config, validate=False)

    quote_currencies = args.get("quote_currencies")
    if not quote_currencies:
        quote_currencies = [config.get("stake_currency")]
    results = {}
    with FtNoDBContext():
        for curr in quote_currencies:
            config["stake_currency"] = curr
            pairlists = PairListManager(exchange, config)
            pairlists.refresh_pairlist()
            results[curr] = pairlists.whitelist

    for curr, pairlist in results.items():
        if not args.get("print_one_column", False) and not args.get("list_pairs_print_json", False):
            print(f"Pairs for {curr}: ")

        if args.get("print_one_column", False):
            print("\n".join(pairlist))
        elif args.get("list_pairs_print_json", False):
            print(rapidjson.dumps(list(pairlist), default=str))
        else:
            print(pairlist)

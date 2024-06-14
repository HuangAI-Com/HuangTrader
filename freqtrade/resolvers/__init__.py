# flake8: noqa: F401
# isort: off
from HuangTrader.resolvers.iresolver import IResolver
from HuangTrader.resolvers.exchange_resolver import ExchangeResolver

# isort: on
# Don't import HyperoptResolver to avoid loading the whole Optimize tree
# from HuangTrader.resolvers.hyperopt_resolver import HyperOptResolver
from HuangTrader.resolvers.pairlist_resolver import PairListResolver
from HuangTrader.resolvers.protection_resolver import ProtectionResolver
from HuangTrader.resolvers.strategy_resolver import StrategyResolver

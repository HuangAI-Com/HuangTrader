# flake8: noqa: F401
"""
Commands module.
Contains all start-commands, subcommands and CLI Interface creation.

Note: Be careful with file-scoped imports in these subfiles.
    as they are parsed on startup, nothing containing optional modules should be loaded.
"""

from HuangTrader.commands.analyze_commands import start_analysis_entries_exits
from HuangTrader.commands.arguments import Arguments
from HuangTrader.commands.build_config_commands import start_new_config, start_show_config
from HuangTrader.commands.data_commands import (
    start_convert_data,
    start_convert_trades,
    start_download_data,
    start_list_data,
)
from HuangTrader.commands.db_commands import start_convert_db
from HuangTrader.commands.deploy_commands import (
    start_create_userdir,
    start_install_ui,
    start_new_strategy,
)
from HuangTrader.commands.hyperopt_commands import start_hyperopt_list, start_hyperopt_show
from HuangTrader.commands.list_commands import (
    start_list_exchanges,
    start_list_freqAI_models,
    start_list_markets,
    start_list_strategies,
    start_list_timeframes,
    start_show_trades,
)
from HuangTrader.commands.optimize_commands import (
    start_backtesting,
    start_backtesting_show,
    start_edge,
    start_hyperopt,
    start_lookahead_analysis,
    start_recursive_analysis,
)
from HuangTrader.commands.pairlist_commands import start_test_pairlist
from HuangTrader.commands.plot_commands import start_plot_dataframe, start_plot_profit
from HuangTrader.commands.strategy_utils_commands import start_strategy_update
from HuangTrader.commands.trade_commands import start_trading
from HuangTrader.commands.webserver_commands import start_webserver

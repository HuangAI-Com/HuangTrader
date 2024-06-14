from typing import Any, Dict

from HuangTrader.configuration import setup_utils_configuration
from HuangTrader.enums import RunMode
from HuangTrader.exceptions import ConfigurationError


def validate_plot_args(args: Dict[str, Any]) -> None:
    if not args.get("datadir") and not args.get("config"):
        raise ConfigurationError(
            "You need to specify either `--datadir` or `--config` "
            "for plot-profit and plot-dataframe."
        )


def start_plot_dataframe(args: Dict[str, Any]) -> None:
    """
    Entrypoint for dataframe plotting
    """
    # Import here to avoid errors if plot-dependencies are not installed.
    from HuangTrader.plot.plotting import load_and_plot_trades

    validate_plot_args(args)
    config = setup_utils_configuration(args, RunMode.PLOT)

    load_and_plot_trades(config)


def start_plot_profit(args: Dict[str, Any]) -> None:
    """
    Entrypoint for plot_profit
    """
    # Import here to avoid errors if plot-dependencies are not installed.
    from HuangTrader.plot.plotting import plot_profit

    validate_plot_args(args)
    config = setup_utils_configuration(args, RunMode.PLOT)

    plot_profit(config)

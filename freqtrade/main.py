#!/usr/bin/env python3
"""
Main HuangTrader bot script.
Read the documentation to know what cli arguments you need.
"""

import logging
import sys
from typing import Any, List, Optional


# check min. python version
if sys.version_info < (3, 9):  # pragma: no cover
    sys.exit("HuangTrader requires Python version >= 3.9")

from HuangTrader import __version__
from HuangTrader.commands import Arguments
from HuangTrader.constants import DOCS_LINK
from HuangTrader.exceptions import ConfigurationError, HuangTraderException, OperationalException
from HuangTrader.loggers import setup_logging_pre
from HuangTrader.util.gc_setup import gc_set_threshold


logger = logging.getLogger("HuangTrader")


def main(sysargv: Optional[List[str]] = None) -> None:
    """
    This function will initiate the bot and start the trading loop.
    :return: None
    """

    return_code: Any = 1
    try:
        setup_logging_pre()
        arguments = Arguments(sysargv)
        args = arguments.get_parsed_arg()

        # Call subcommand.
        if "func" in args:
            logger.info(f"HuangTrader {__version__}")
            gc_set_threshold()
            return_code = args["func"](args)
        else:
            # No subcommand was issued.
            raise OperationalException(
                "Usage of HuangTrader requires a subcommand to be specified.\n"
                "To have the bot executing trades in live/dry-run modes, "
                "depending on the value of the `dry_run` setting in the config, run HuangTrader "
                "as `HuangTrader trade [options...]`.\n"
                "To see the full list of options available, please use "
                "`HuangTrader --help` or `HuangTrader <command> --help`."
            )

    except SystemExit as e:  # pragma: no cover
        return_code = e
    except KeyboardInterrupt:
        logger.info("SIGINT received, aborting ...")
        return_code = 0
    except ConfigurationError as e:
        logger.error(
            f"Configuration error: {e}\n"
            f"Please make sure to review the documentation at {DOCS_LINK}."
        )
    except HuangTraderException as e:
        logger.error(str(e))
        return_code = 2
    except Exception:
        logger.exception("Fatal exception!")
    finally:
        sys.exit(return_code)


if __name__ == "__main__":  # pragma: no cover
    main()

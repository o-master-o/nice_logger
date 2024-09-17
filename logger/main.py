import logging
import time

from rich.console import Console
from rich.logging import RichHandler


__all__ = ['RichLogger', 'logger']


class MillisecondFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        created = self.converter(record.created)
        if datefmt:
            s = time.strftime(datefmt, created)
            s = s.replace('%f', f'{int(record.msecs):03d}')
            return s
        else:
            return super(MillisecondFormatter, self).formatTime(record, datefmt)


class RichConsoleHandler(RichHandler):
    LOG_STYLES = {
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold blink magenta"
    }

    LEVEL_SHORTCUTS = {
        "DEBUG": "DBG",
        "INFO": "INF",
        "WARNING": "WRN",
        "ERROR": "ERR",
        "CRITICAL": "CRT"
    }

    def __init__(self, *args, **kwargs):
        self.console = Console()
        super().__init__(*args, console=self.console, **kwargs)
        self.setFormatter(MillisecondFormatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S.%f"))

    def emit(self, record):
        self.console.print(self._format_message(record))

    def _format_message(self, record):
        self.format(record)
        record.levelname.ljust(8)
        formatted_message = f"{record.asctime} {self._styled_level_name(record)} {record.message}"
        return formatted_message

    def _styled_level_name(self, record):
        return f"[{self._set_style(record)}]|{self._set_log_level_name(record)}|[/]"

    def _set_log_level_name(self, record):
        return self.LEVEL_SHORTCUTS.get(record.levelname, self.LEVEL_SHORTCUTS["DEBUG"])

    def _set_style(self, record):
        return self.LOG_STYLES.get(record.levelname, "white")


class RichLogger(logging.Logger):

    def __init__(self, name="rich_logger", level=logging.NOTSET):
        super().__init__(name, level)
        self.propagate = False
        self.addHandler(RichConsoleHandler())

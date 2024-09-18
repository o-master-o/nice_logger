from logger.main import RichLogger

logger = RichLogger()


logger.info("Some normal text")
logger.info("[blue]Some [red]rich [violet]marked[not violet] [yellow]colored [green]text[/]")
logger.info("Automatically colored /path/to/some_file.txt or {'some': 'dict', 'structure': 55}")
logger.info("Automatically colored date 2025-02-21 20:23:21, list [1, 2, 'value'], etc.")

logger.debug("Some dubug log")
logger.warning("Some warning log")
logger.error("Some error log")
logger.critical("Some critical log")

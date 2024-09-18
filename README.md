# Rich Logger

## Overview
This custom logger extends Python's built-in logging module by integrating with the rich library to provide a more visually appealing and informative logging experience. The logger is designed to be easy to use while offering advanced features like millisecond precision in timestamps and color-coded log levels for better readability.

---
## Features
Rich Formatting: Utilizes rich.console.Console for enhanced formatting.
Millisecond Precision: Custom formatter to include milliseconds in log timestamps.
Color-Coded Log Levels: Different colors for each log level for easy distinction.
Level Name Shortcuts: Abbreviated log level names for compact and clear logs.
Customizable: Easy to integrate and customize in any Python project.

---
## Installation
Before using the custom logger, ensure you have the rich library installed. If not, you can install it using pip:
```commandline
pip install rich
```

---
## Usage
To use the custom logger in your Python application, simply import and instantiate RichLogger. Example:
```python
from custom_logger_module import RichLogger

logger = RichLogger()
logger.info("This is an info message")

```
### Output example

from rich import console
from .version import __version__

console = console.Console()
console.show_cursor(False)
console.set_window_title(f"RequiemBot v{__version__}")
from rich.console import Console
from rich.text import Text
import time

console = Console()

mesaje = "Hola, futuro/a programador/a"

for letra in mesaje:
    console.print(Text(letra, style="bold magenta"), end="")
    time.sleep(0.1)
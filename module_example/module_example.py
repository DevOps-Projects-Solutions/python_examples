#importing modules​

from greetings import say_hello # Custom module​

from datetime import datetime # Built-in module​

from rich.console import Console # Third-party module (rich)​

# Create a console for colorful and formatted output​

console = Console()

# Get user input​

name = input("What's your name? ")

# Use custom module​

greeting = say_hello(name)

# Print the greeting with rich styling​

console.print(f"[bold green]{greeting}[/bold green]")

# Use built-in module to display the current time​

now = datetime.now()

console.print(f"[bold blue]The current date and time is: {now.strftime('%Y-%m-%d %H:%M:%S')}[/bold blue]")
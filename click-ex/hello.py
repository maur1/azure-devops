import click

@click.command(help="This is just a hello app. It does nothing.")
@click.option("--name", prompt="I need your name", help="Need name")
@click.option("--color", prompt="I need your color", help="This is your color")
def hello(name, color):
    if name == "Maureen":
        click.echo("Maureen, you are always yellow.")
        click.echo(click.style(f"Hello {name}!", fg="yellow"))
    else:
        click.echo(click.style(f"Hello {name}!", fg=color))
''
if __name__ == "__main__":
    hello()
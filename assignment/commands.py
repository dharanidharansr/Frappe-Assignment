import click


@click.command()
def wow():
    click.echo("Hello from the custom Bench CLI!!")


@click.command("hello-app")
def hello_app():
    click.echo("Hello from custom command!")


commands = [wow, hello_app]
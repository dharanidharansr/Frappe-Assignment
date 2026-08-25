import click

@click.command()
def wow():
    click.echo("Hello from the custom Bench CLI!!")
    
commands = [wow]
